# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Auth.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from . import res_rc


class Ui_Authorization(QtWidgets.QDialog):
	def setupUi(self, Authorization):
		Authorization.setObjectName("Authorization")
		Authorization.resize(225, 201)
		Authorization.setMinimumSize(QtCore.QSize(225, 201))
		Authorization.setMaximumSize(QtCore.QSize(225, 201))
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(":/app_icons/icons/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		Authorization.setWindowIcon(icon)
		Authorization.setStyleSheet("QLabel {\n"
"font: 75 12pt \"Calibri\";\n"
"}\n"
"\n"
"QCheckBox {\n"
"font: 75 12pt \"Calibri\";\n"
"}\n"
"\n"
"QDialog {\n"
"background-color:rgb(229, 229, 229);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: rgb(215, 215, 215);\n"
"border: none;\n"
"font: 10pt \"MS Sans\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(204, 204, 204);\n"
"}\n"
"\n"
"QLineEdit {\n"
"border:None;\n"
"}")
		self.login_label = QtWidgets.QLabel(Authorization)
		self.login_label.setGeometry(QtCore.QRect(20, 10, 121, 21))
		self.login_label.setMinimumSize(QtCore.QSize(121, 21))
		self.login_label.setMaximumSize(QtCore.QSize(121, 21))
		font = QtGui.QFont()
		font.setFamily("Calibri")
		font.setPointSize(12)
		font.setBold(False)
		font.setItalic(False)
		font.setWeight(9)
		self.login_label.setFont(font)
		self.login_label.setStyleSheet("")
		self.login_label.setObjectName("login_label")
		self.login_line = QtWidgets.QLineEdit(Authorization)
		self.login_line.setGeometry(QtCore.QRect(20, 35, 181, 21))
		self.login_line.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
		self.login_line.setAcceptDrops(False)
		self.login_line.setStyleSheet("")
		self.login_line.setInputMask("")
		self.login_line.setText("")
		self.login_line.setMaxLength(30)
		self.login_line.setFrame(True)
		self.login_line.setObjectName("login_line")
		self.password_label = QtWidgets.QLabel(Authorization)
		self.password_label.setEnabled(True)
		self.password_label.setGeometry(QtCore.QRect(20, 70, 121, 16))
		font = QtGui.QFont()
		font.setFamily("Calibri")
		font.setPointSize(12)
		font.setBold(False)
		font.setItalic(False)
		font.setWeight(9)
		self.password_label.setFont(font)
		self.password_label.setStyleSheet("")
		self.password_label.setObjectName("password_label")
		self.password_line = QtWidgets.QLineEdit(Authorization)
		self.password_line.setGeometry(QtCore.QRect(20, 95, 161, 21))
		self.password_line.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
		self.password_line.setAcceptDrops(False)
		self.password_line.setStyleSheet("")
		self.password_line.setInputMask("")
		self.password_line.setText("")
		self.password_line.setMaxLength(30)
		self.password_line.setFrame(True)
		self.password_line.setEchoMode(QtWidgets.QLineEdit.Normal)
		self.password_line.setObjectName("password_line")
		self.show_password = QtWidgets.QPushButton(Authorization)
		self.show_password.setEnabled(True)
		self.show_password.setGeometry(QtCore.QRect(180, 95, 20, 20))
		self.show_password.setStyleSheet("QPushButton {\n"
"background-color: rgb(229, 229, 229);\n"
"}")
		self.show_password.setText("")
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap(":/app_icons/icons/unvisib.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.show_password.setIcon(icon1)
		self.show_password.setObjectName("show_password")
		self.checktosave = QtWidgets.QCheckBox(Authorization)
		self.checktosave.setGeometry(QtCore.QRect(110, 130, 91, 20))
		self.checktosave.setCheckable(True)
		self.checktosave.setChecked(True)
		self.checktosave.setAutoExclusive(False)
		self.checktosave.setTristate(False)
		self.checktosave.setObjectName("checktosave")
		self.save_btn = QtWidgets.QPushButton(Authorization)
		self.save_btn.setGeometry(QtCore.QRect(130, 170, 75, 23))
		self.save_btn.setObjectName("save_btn")
		self.cancel_btn = QtWidgets.QPushButton(Authorization)
		self.cancel_btn.setGeometry(QtCore.QRect(20, 170, 75, 23))
		self.cancel_btn.setObjectName("cancel_btn")

		self.retranslateUi(Authorization)
		QtCore.QMetaObject.connectSlotsByName(Authorization)

	def retranslateUi(self, Authorization):
		_translate = QtCore.QCoreApplication.translate
		Authorization.setWindowTitle(_translate("Authorization", "Authorization"))
		self.login_label.setText(_translate("Authorization", "Логин:"))
		self.password_label.setText(_translate("Authorization", "Пароль:"))
		self.checktosave.setText(_translate("Authorization", "Сохранить"))
		self.save_btn.setText(_translate("Authorization", "Готово"))
		self.cancel_btn.setText(_translate("Authorization", "Отмена"))