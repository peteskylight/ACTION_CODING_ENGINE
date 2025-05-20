from PySide6.QtCore import QObject, QThread, Signal
import yagmail

class EmailSendingWorker(QObject):
    finished = Signal()
    error = Signal(str)

    def __init__(self, receipient, session_name, attachment_directory, front_video_directory, center_video_directory, time_exported):
        super().__init__()
        self.gmail_app_password = "tsjg hxwv xhfn vphw"
        self.gmail_address = "action.coding.engine.cpe@gmail.com"
        self.yagmail_SMTP = yagmail.SMTP(self.gmail_address, self.gmail_app_password)

        self.receipient = receipient
        self.session_name = session_name
        self.attachment_directory = attachment_directory
        self.front_video_directory = front_video_directory
        self.center_video_directory = center_video_directory
        self.time_exported = time_exported

    def run(self):
        try:
            self.yagmail_SMTP.send(
                to=self.receipient,
                subject=f"ACE: Report Summary for Session: {self.session_name}",
                contents=(
                    "Good day!\n\n"
                    "Thank you for using Action Coding Engine (ACE)!\n\n"
                    "We have sent you the generated reports of visualized actions based on the imported videos:\n\n"
                    f"Front Video: {self.front_video_directory}\n"
                    f"Center Video: {self.center_video_directory}\n\n"
                    f"Time Exported: {self.time_exported}"
                ),
                attachments=self.attachment_directory
            )
            self.finished.emit()
        except Exception as e:
            self.error.emit(str(e))
