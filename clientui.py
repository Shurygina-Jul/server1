# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'messenger.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_My_messenger(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, My_messenger):
        My_messenger.setObjectName("My_messenger")
        My_messenger.resize(447, 499)
        self.centralwidget = QtWidgets.QWidget(My_messenger)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(324, 412, 81, 31))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 20, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLineWidth(8)
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(40, 110, 361, 281))
        self.textBrowser.setObjectName("textBrowser")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(40, 70, 161, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(250, 70, 151, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(40, 410, 241, 31))
        self.textEdit.setObjectName("textEdit")
        My_messenger.setCentralWidget(self.centralwidget)

        self.retranslateUi(My_messenger)
        QtCore.QMetaObject.connectSlotsByName(My_messenger)

    def retranslateUi(self, My_messenger):
        _translate = QtCore.QCoreApplication.translate
        My_messenger.setWindowTitle(_translate("My_messenger", "My_messenger"))
        self.pushButton.setText(_translate("My_messenger", "Send"))
        self.label.setText(_translate("My_messenger", "My messenger"))
        self.lineEdit.setPlaceholderText(_translate("My_messenger", "Username"))
        self.lineEdit_2.setPlaceholderText(_translate("My_messenger", "Password"))
        self.textEdit.setPlaceholderText(_translate("My_messenger", "Type massage"))

app = QtWidgets.QApplication([])
window = Ui_My_messenger()
window.show()
app.exec_()