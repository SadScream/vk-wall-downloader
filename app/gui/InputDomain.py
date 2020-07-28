# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inputDomain.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

try:
	from . import res_rc
except:
	import res_rc


class Ui_InputDomain(QtWidgets.QDialog):
	def setupUi(self, InputDomain):
		InputDomain.setObjectName("InputDomain")
		InputDomain.resize(261, 91)
		InputDomain.setMinimumSize(QtCore.QSize(261, 91))
		InputDomain.setMaximumSize(QtCore.QSize(261, 91))
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(":/app_icons/icons/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		InputDomain.setWindowIcon(icon)
		InputDomain.setStyleSheet("QPushButton {\n"
"background-color: rgb(215, 215, 215);\n"
"border: none;\n"
"font: 10pt \"MS Sans\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(204, 204, 204);\n"
"}\n"
"\n"
"QDialog {\n"
"background-color:rgb(229, 229, 229);\n"
"}")
		self.cancel_btn = QtWidgets.QPushButton(InputDomain)
		self.cancel_btn.setGeometry(QtCore.QRect(180, 60, 75, 23))
		self.cancel_btn.setObjectName("cancel_btn")
		self.ok_btn = QtWidgets.QPushButton(InputDomain)
		self.ok_btn.setGeometry(QtCore.QRect(100, 60, 75, 23))
		self.ok_btn.setObjectName("ok_btn")
		self.group_name = QtWidgets.QLineEdit(InputDomain)
		self.group_name.setGeometry(QtCore.QRect(10, 30, 113, 20))
		self.group_name.setStyleSheet("QLineEdit {\n"
"border:None;\n"
"}")
		self.group_name.setObjectName("group_name")
		self.group_domain = QtWidgets.QLineEdit(InputDomain)
		self.group_domain.setGeometry(QtCore.QRect(140, 30, 113, 20))
		self.group_domain.setStyleSheet("QLineEdit {\n"
"border:None;\n"
"}")
		self.group_domain.setObjectName("group_domain")
		self.label = QtWidgets.QLabel(InputDomain)
		self.label.setGeometry(QtCore.QRect(10, 10, 61, 16))
		self.label.setObjectName("label")
		self.label_2 = QtWidgets.QLabel(InputDomain)
		self.label_2.setGeometry(QtCore.QRect(140, 10, 61, 16))
		self.label_2.setObjectName("label_2")

		self.retranslateUi(InputDomain)
		QtCore.QMetaObject.connectSlotsByName(InputDomain)

	def retranslateUi(self, InputDomain):
		_translate = QtCore.QCoreApplication.translate
		InputDomain.setWindowTitle(_translate("InputDomain", "Domain item"))
		self.cancel_btn.setText(_translate("InputDomain", "Отмена"))
		self.ok_btn.setText(_translate("InputDomain", "Готово"))
		self.label.setText(_translate("InputDomain", "Name:"))
		self.label_2.setText(_translate("InputDomain", "Domain:"))
