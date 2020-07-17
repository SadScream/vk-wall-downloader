# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Settings.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from . import res_rc


class Input(QtWidgets.QLineEdit):

	def __init__(self, parent):
		super().__init__(parent)
		self.parent = parent
		self.last_text = None


	def keyPressEvent(self, e:QtCore.QEvent):
		if e.key() == 16777223: # delete
			if len(self.text()):
				self.last_text = self.text()

			self.setText("")

		elif e.key() == 90 and e.modifiers() == QtCore.Qt.ControlModifier: # ctrl+z
			if self.last_text:
				self.setText(self.last_text)
				self.last_text = None

		else:
			e.ignore()


class Ui_Settings(QtWidgets.QDialog):
	def setupUi(self, Settings):
		Settings.setObjectName("Settings")
		Settings.resize(341, 121)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(":/app_icons/icons/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		Settings.setWindowIcon(icon)
		Settings.setStyleSheet("QDialog {\n"
"background: rgb(234, 234, 234);\n"
"}")
		self.path = Input(Settings)
		self.path.setGeometry(QtCore.QRect(110, 10, 171, 20))
		self.path.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
		self.path.setAcceptDrops(False)
		self.path.setStyleSheet("QLineEdit {\n"
"background: white;\n"
"border: None\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"background: rgb(225, 225, 225);\n"
"}")
		self.path.setObjectName("path")
		self.path_btn = QtWidgets.QPushButton(Settings)
		self.path_btn.setGeometry(QtCore.QRect(290, 10, 41, 20))
		self.path_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(211, 211, 211);\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(219, 219, 219);\n"
"}")
		self.path_btn.setObjectName("path_btn")
		self.label = QtWidgets.QLabel(Settings)
		self.label.setGeometry(QtCore.QRect(10, 10, 91, 16))
		self.label.setStyleSheet("QLabel {\n"
"font: 12pt  \"Calibri\";\n"
"border: none;\n"
"}")
		self.label.setObjectName("label")
		self.ok_btn = QtWidgets.QPushButton(Settings)
		self.ok_btn.setGeometry(QtCore.QRect(260, 90, 75, 23))
		self.ok_btn.setStyleSheet("QPushButton {\n"
"background-color: rgb(211, 211, 211);\n"
"border: none;\n"
"font: 10pt \"MS Sans\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(219, 219, 219);\n"
"}")
		self.ok_btn.setObjectName("ok_btn")
		self.cancel_btn = QtWidgets.QPushButton(Settings)
		self.cancel_btn.setGeometry(QtCore.QRect(180, 90, 75, 23))
		self.cancel_btn.setStyleSheet("QPushButton {\n"
"background-color: rgb(211, 211, 211);\n"
"border: none;\n"
"font: 10pt \"MS Sans\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(219, 219, 219);\n"
"}")
		self.cancel_btn.setObjectName("cancel_btn")
		self.to_remember = QtWidgets.QCheckBox(Settings)
		self.to_remember.setGeometry(QtCore.QRect(240, 40, 101, 20))
		self.to_remember.setStyleSheet("QCheckBox {\n"
"font: 12pt \"Calibri\";\n"
"}")
		self.to_remember.setCheckable(True)
		self.to_remember.setChecked(True)
		self.to_remember.setAutoExclusive(False)
		self.to_remember.setTristate(False)
		self.to_remember.setObjectName("to_remember")

		self.retranslateUi(Settings)
		QtCore.QMetaObject.connectSlotsByName(Settings)

	def retranslateUi(self, Settings):
		_translate = QtCore.QCoreApplication.translate
		Settings.setWindowTitle(_translate("Settings", "Settings"))
		self.path.setPlaceholderText(_translate("Settings", "Press \'Delete\' to clear this field"))
		self.path_btn.setText(_translate("Settings", "..."))
		self.label.setToolTip(_translate("Settings", "<html><head/><body><p>В указанной директории создастся папка Folders, в которую в свою очередь будут сохраняться последующие папки сообществ. Если оставить это поле пустым, то папка создастся в директории с главным файлом app.py</p></body></html>"))
		self.label.setWhatsThis(_translate("Settings", "<html><head/><body><p><br/></p></body></html>"))
		self.label.setText(_translate("Settings", "Директория:"))
		self.ok_btn.setText(_translate("Settings", "Готово"))
		self.cancel_btn.setText(_translate("Settings", "Отмена"))
		self.to_remember.setText(_translate("Settings", "Запомнить"))


	
class Settings(Ui_Settings):

	def __init__(self, config):
		super().__init__()
		self.setupUi(self)
		self.setFocus()
		self.config = config

		self.constructor()

	def constructor(self):
		self.config_pth = self.config.read("path_to")

		if self.config_pth == None:
			self.path.setText("")
		else:
			self.path.setText(self.config_pth)

		self.ok_btn.clicked.connect(self.ok_clicked)
		self.cancel_btn.clicked.connect(self.cancel_clicked)
		self.path_btn.clicked.connect(self.open_path)

	def Open(self):
		return self.exec_()

	def ok_clicked(self):
		if self.to_remember.isChecked() and len(self.path.text()):
			self.config.write("path_to", self.path.text())
		elif self.to_remember.isChecked() and not len(self.path.text()):
			self.config.write("path_to", None)

		self.config.write("remember", self.to_remember.isChecked())
		self.close()

	def cancel_clicked(self):
		self.path.setText(self.config.read("path_to"))
		self.to_remember.setChecked(self.config.read("remember"))
		self.close()

	def open_path(self):
		path = "C:/"

		if self.config_pth == None:
			pass
		else:
			path = self.path.text()

		directory = QtWidgets.QFileDialog.getExistingDirectory(parent=None, directory=path, options=QtWidgets.QFileDialog.ShowDirsOnly)

		if directory != '':
			self.path.setText(directory)
