import sys
import webbrowser
import DuplicateChecker
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QHBoxLayout, QListView, QListWidgetItem, QPushButton, QWidget, QLabel, QListWidget, QVBoxLayout , QTextEdit, QMessageBox

class EntryWidget(QWidget):
    def __init__(self, entry: str, entryNumber: int):
        super().__init__()
        self.entry = entry
        masterLayout = QHBoxLayout()
        self.setLayout(masterLayout)
        numberLabel = QLabel(str(entryNumber))
        numberLabel.setFixedWidth(20)
        masterLayout.addWidget(numberLabel)

        goToLinkBtn = QPushButton(f"{entry}")
        masterLayout.addWidget(goToLinkBtn)
        goToLinkBtn.clicked.connect(self.GoToLinkBtnClicked)
        goToLinkBtn.setStyleSheet('text-align: left;')

    def GoToLinkBtnClicked(self):
        webbrowser.open(self.entry)


class DulicateCheckApp(QWidget):
    def __init__(self):
        super().__init__()
        self.checker = DuplicateChecker.DuplicateChecker()
        masterLayout = QVBoxLayout()
        self.setLayout(masterLayout)

        label = QLabel("Paste in your addresses:")
        masterLayout.addWidget(label)

        self.importText = QTextEdit()
        masterLayout.addWidget(self.importText)
        self.importText.setFixedHeight(50)
        
        self.entryList = QListWidget()
        masterLayout.addWidget(self.entryList)

        buttonsLayout = QHBoxLayout()
        masterLayout.addLayout(buttonsLayout)

        checkBtn = QPushButton("Process And Check")
        buttonsLayout.addWidget(checkBtn)
        checkBtn.clicked.connect(self.CheckBtnClicked)

        clearBtn = QPushButton("Clear")
        buttonsLayout.addWidget(clearBtn)
        clearBtn.clicked.connect(self.ClearBtnClicked)

        self.dupList = QListWidget()
        masterLayout.addWidget(self.dupList)
        self.setMinimumWidth(800)

    def ClearBtnClicked(self):
        self.importText.clear()
        self.entryList.clear()
        self.dupList.clear()

    def CheckBtnClicked(self):
        self.dupList.clear()
        text = self.importText.toPlainText()
        self.checker.SetEntries(text, ',')

        self.UpdateEntryList()
        self.UpdateDupList()

    def UpdateEntryList(self):
        self.entryList.clear()
        for index, entry in enumerate(self.checker.GetEntries()):
            item = QListWidgetItem()
            item.setData(Qt.UserRole, entry)
            self.entryList.addItem(item)
            itemWidget = EntryWidget(entry,index + 1)
            self.entryList.setItemWidget(item, itemWidget)
            item.setSizeHint(itemWidget.sizeHint())


    def UpdateDupList(self):
        #update duplist
        dupRec = self.checker.FindDuplicates()

        if len(dupRec) == 0:
            QMessageBox.information(self, "Message", f"No Duplicate Found! \ntotal count is: {len(self.checker.GetEntries())}")
            return

        for dup, count in dupRec.items():
            info = f"---------------------------------------------------------------------------\n{dup}\nRepeated: {count} times!\n---------------------------------------------------------------------------"
            self.dupList.addItem(info)


app = QApplication()

checkApp = DulicateCheckApp()
checkApp.show()

sys.exit(app.exec())
