# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 452)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.encodeBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.encodeBtn.setGeometry(QtCore.QRect(240, 350, 121, 31))
        self.encodeBtn.setObjectName("encodeBtn")
        self.decodeBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.decodeBtn.setGeometry(QtCore.QRect(420, 90, 121, 31))
        self.decodeBtn.setObjectName("decodeBtn")
        self.userInput = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.userInput.setGeometry(QtCore.QRect(30, 50, 331, 261))
        self.userInput.setObjectName("userInput")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 331, 21))
        self.label.setObjectName("label")
        self.fileSavedAtLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.fileSavedAtLabel.setGeometry(QtCore.QRect(40, 380, 321, 16))
        self.fileSavedAtLabel.setText("")
        self.fileSavedAtLabel.setObjectName("fileSavedAtLabel")
        self.selectMethod = QtWidgets.QComboBox(parent=self.centralwidget)
        self.selectMethod.setGeometry(QtCore.QRect(30, 350, 181, 31))
        self.selectMethod.setObjectName("selectMethod")
        self.selectMethod.addItem("")
        self.selectMethod.addItem("")
        self.selectMethod.addItem("")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 320, 121, 21))
        self.label_2.setObjectName("label_2")
        self.browseLineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.browseLineEdit.setGeometry(QtCore.QRect(420, 50, 201, 31))
        self.browseLineEdit.setObjectName("browseLineEdit")
        self.browseBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.browseBtn.setGeometry(QtCore.QRect(630, 50, 121, 31))
        self.browseBtn.setObjectName("browseBtn")
        self.decodedMessage = QtWidgets.QLabel(parent=self.centralwidget)
        self.decodedMessage.setGeometry(QtCore.QRect(420, 170, 331, 211))
        self.decodedMessage.setAutoFillBackground(False)
        self.decodedMessage.setStyleSheet("background-color: white;  border: 0.5px solid black")
        self.decodedMessage.setText("")
        self.decodedMessage.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.decodedMessage.setObjectName("decodedMessage")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(420, 20, 331, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(420, 140, 331, 21))
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TextStegano"))
        self.encodeBtn.setText(_translate("MainWindow", "Encode"))
        self.decodeBtn.setText(_translate("MainWindow", "Decode"))
        self.label.setText(_translate("MainWindow", "Input your message:"))
        self.selectMethod.setItemText(0, _translate("MainWindow", "Spacing"))
        self.selectMethod.setItemText(1, _translate("MainWindow", "Background Color"))
        self.selectMethod.setItemText(2, _translate("MainWindow", "Letter Color"))
        self.label_2.setText(_translate("MainWindow", "Select method:"))
        self.browseBtn.setText(_translate("MainWindow", "Browse"))
        self.label_4.setText(_translate("MainWindow", "Input encoded file:"))
        self.label_5.setText(_translate("MainWindow", "Decoded message:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
