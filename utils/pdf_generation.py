import os
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer, Paragraph
from reportlab.lib.pagesizes import landscape, A4, letter
from reportlab.lib import colors
from collections import defaultdict

def export_logs_to_pdf(self, tables, filename="logs_export.pdf"):
    """
    Exports log tables to a PDF file with raw detection times and sorted order.
    """
    output_dir = os.path.join(os.path.dirname(__file__), "..", "outputs")
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, filename)

    if not tables:
        print("No data to export.")
        return

    doc = SimpleDocTemplate(file_path, pagesize=letter)  # Portrait mode
    elements = []
    styles = getSampleStyleSheet()

    # Add Title
    elements.append(Paragraph("Log Summary Report", styles['Title']))
    elements.append(Spacer(1, 12))

    summary_dict = defaultdict(lambda: {"instances": 0, "start_time": float("inf"), "end_time": float("-inf")})

    table_titles = [
        "Sitting and Leaning on Desk",
        "Turning Around",
        "Standing, Extending Arm"
    ]

    for table, title in zip(tables, table_titles):
        if table.rowCount() == 0:
            continue
        elements.append(Paragraph("To be edited paragraph cause we plan to add something soon", styles['Normal']))
        elements.append(Paragraph(title, styles['Heading2']))

        headers = ["Person ID", "Action", "Raw Detection Time (s)"]
        raw_data = []

        for row in range(table.rowCount()):
            person_id = table.item(row, 0).text().strip() if table.item(row, 0) else "Unknown"
            action = table.item(row, 1).text().strip() if table.item(row, 1) else "Unknown"
            duration_text = table.item(row, 2).text().strip() if table.item(row, 2) else "0.0"

            try:
                start_time = float(duration_text.replace("s", "").strip())  # Use raw detection time
                raw_data.append([person_id, action, f"{start_time:.2f}s"])

                # Update summary dictionary
                key = (person_id, action)
                summary_dict[key]["instances"] += 1
                summary_dict[key]["start_time"] = min(summary_dict[key]["start_time"], start_time)
                summary_dict[key]["end_time"] = max(summary_dict[key]["end_time"], start_time)

            except ValueError:
                print(f"Warning: Invalid duration '{duration_text}' for {person_id}, {action}. Skipping.")
                continue  # Skip invalid entries

        # Sort by **Time First**, then **Person ID**
        raw_data.sort(key=lambda x: (float(x[2].replace("s", "")), x[0]))

        # Create a Table for Each Section
        section_table = Table([headers] + raw_data, colWidths=[80, 120, 150])
        section_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold')
        ]))

        elements.append(section_table)
        elements.append(Spacer(1, 18))

    # Convert summary dictionary to sorted list
    summary_headers = ["Person ID", "Action", "Instances", "Timestamp (s)"]
    formatted_logs = []

    for (person, action), times in summary_dict.items():
        if times["start_time"] == float("inf") or times["end_time"] == float("-inf"):
            continue  # Skip invalid entries

        timestamp = f"{times['start_time']:.2f}s - {times['end_time']:.2f}s"
        formatted_logs.append([person, action, str(times["instances"]), timestamp])

    # **Sort summary table by Person ID first, then by Time**
    formatted_logs.sort(key=lambda x: (x[0], float(x[3].split("s")[0])))

    # Create Summary Table
    summary_table = Table([summary_headers] + formatted_logs, colWidths=[80, 120, 80, 150])
    summary_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold')
    ]))
    elements.insert(2, Paragraph("To be edited paragraph cause we plan to add something soon", styles['Normal']))
    elements.insert(3, summary_table)  # Insert summary before log tables
    elements.insert(4, Spacer(1, 18))

    doc.build(elements)
    print(f"PDF saved as {filename}")

def handle_export_logs(self):
    tables = [self.main_window.ai_analytics_event_logs_table_1, self.main_window.ai_analytics_event_logs_table_2, self.main_window.ai_analytics_event_logs_table_3]
    tables = [table for table in tables if table]  # Remove None tables

    action_timeline = defaultdict(lambda: {"first": None, "last": None})

    for table in tables:
        if table.rowCount() == 0:
            continue  # Skip empty tables
        
        for row in range(table.rowCount()):
            person = table.item(row, 0).text().strip() if table.item(row, 0) else "Unknown Person"
            action = table.item(row, 1).text().strip() if table.item(row, 1) else "Unknown Action"
            start_time_text = table.item(row, 2).text().strip() if table.item(row, 2) else "0"

            # Convert to float
            try:
                start_time = float(start_time_text.replace("s", "").strip())
            except ValueError:
                continue  # Skip invalid time values

            key = (person, action)

            # Ensure first time is set properly
            if action_timeline[key]["first"] is None or start_time < action_timeline[key]["first"]:
                action_timeline[key]["first"] = start_time
            
            # Always update last occurrence (ensuring it's greater than first)
            if action_timeline[key]["last"] is None or start_time > action_timeline[key]["last"]:
                action_timeline[key]["last"] = start_time

    # Sort actions by extracted number
    def extract_person_number(person_id):
        digits = "".join(filter(str.isdigit, person_id))
        return int(digits) if digits else float("inf")

    sorted_timeline = sorted(action_timeline.items(), key=lambda x: extract_person_number(x[0][0]))

    summary_data = []

    # Compute time ranges
    for (person, action), times in sorted_timeline:
        first_time = times["first"]
        last_time = times["last"]
        if first_time is not None and last_time is not None:
            summary_data.append([person, action, f"{first_time:.2f} s → {last_time:.2f} s"])

            # Debugging output
            print(f"✅ {person} - {action} | Start: {first_time} s | End: {last_time} s")

    # Export logs with new summary format
    self.export_logs_to_pdf(tables, "logs_export.pdf")
    print(summary_data)

