import sys

import DuplicateChecker
from PySide6.QtWidgets import QApplication, QHBoxLayout, QPushButton, QWidget, QLabel, QListWidget, QVBoxLayout , QTextEdit, QMessageBox

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
        
        buttonsLayout = QHBoxLayout()
        masterLayout.addLayout(buttonsLayout)

        checkBtn = QPushButton("Check")
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

    def CheckBtnClicked(self):
        self.dupList.clear()
        text = self.importText.toPlainText()
        self.checker.SetEntries(text, ',')
        dupRec = self.checker.FindDuplicates()

        if len(dupRec) == 0:
            QMessageBox.information(self, "Message", f"No Duplicated Found! \ntotal count is: {len(self.checker.getEntries())}")

        for dup, count in dupRec.items():
            info = f"---------------------------------------------------------------------------\n{dup}\nRepeated: {count} times!\n---------------------------------------------------------------------------"
            self.dupList.addItem(info)


app = QApplication()

checkApp = DulicateCheckApp()
checkApp.show()

sys.exit(app.exec())
