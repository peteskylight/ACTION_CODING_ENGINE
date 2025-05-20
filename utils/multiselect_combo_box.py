from PySide6.QtWidgets import QComboBox, QStyledItemDelegate
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QStandardItemModel, QStandardItem

class MultiSelectComboBox(QComboBox):
    # Signal emits a string (list of selected items or "ALL ACTIONS")
    selectionChanged = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setModel(QStandardItemModel(self))
        self.view().pressed.connect(self.handle_item_pressed)
        self.setEditable(True)
        self.lineEdit().setReadOnly(True)
        self.lineEdit().setPlaceholderText("Select actions...")
        self.selected_items = set()
        self.update_text()

    def addItem(self, text):
        item = QStandardItem(text)
        item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsUserCheckable)
        item.setData(Qt.Unchecked, Qt.CheckStateRole)
        self.model().appendRow(item)

    def addItems(self, items):
        for text in items:
            self.addItem(text)

    def handle_item_pressed(self, index):
        item = self.model().itemFromIndex(index)
        if item.checkState() == Qt.Checked:
            item.setCheckState(Qt.Unchecked)
            self.selected_items.discard(item.text())
        else:
            item.setCheckState(Qt.Checked)
            self.selected_items.add(item.text())
        
        self.update_text()

        # Emit a string with selected items or "ALL ACTIONS" if no selection
        selected_text = ", ".join(sorted(self.selected_items)) if self.selected_items else "ALL ACTIONS"
        self.selectionChanged.emit(selected_text)  # Emit the current selection

    def update_text(self):
        text = ", ".join(sorted(self.selected_items)) if self.selected_items else "Select actions..."
        self.lineEdit().setText(text)

    def get_selected_items(self):
        return list(self.selected_items)
    
    def clearSelection(self):
        for i in range(self.model().rowCount()):
            item = self.model().item(i)
            item.setCheckState(Qt.Unchecked)
        self.selected_items.clear()
        self.update_text()

    def selectAll(self):
        for i in range(self.model().rowCount()):
            item = self.model().item(i)
            item.setCheckState(Qt.Checked)
            self.selected_items.add(item.text())
        self.update_text()

