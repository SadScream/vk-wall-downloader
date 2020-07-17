# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Design.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from . import res_rc


class Ui_Main(object):
	def setupUi(self, Main):
		Main.setObjectName("Main")
		Main.resize(441, 242)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(Main.sizePolicy().hasHeightForWidth())
		Main.setSizePolicy(sizePolicy)
		Main.setMinimumSize(QtCore.QSize(441, 242))
		Main.setMaximumSize(QtCore.QSize(441, 242))
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(":/app_icons/icons/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		Main.setWindowIcon(icon)
		Main.setStyleSheet("QMainWindow {\n"
"background: rgb(234, 234, 234);\n"
"}")
		self.centralwidget = QtWidgets.QWidget(Main)
		self.centralwidget.setObjectName("centralwidget")
		self.manual_button = QtWidgets.QRadioButton(self.centralwidget)
		self.manual_button.setGeometry(QtCore.QRect(20, 20, 171, 17))
		self.manual_button.setStyleSheet("QRadioButton {\n"
"font: 11pt  \"Calibri\";\n"
"border: none;\n"
"}")
		self.manual_button.setObjectName("manual_button")
		self.auto_button = QtWidgets.QRadioButton(self.centralwidget)
		self.auto_button.setGeometry(QtCore.QRect(210, 20, 221, 17))
		self.auto_button.setStyleSheet("QRadioButton {\n"
"font: 11pt  \"Calibri\";\n"
"border: none;\n"
"}")
		self.auto_button.setObjectName("auto_button")
		self.domain_label = QtWidgets.QLabel(self.centralwidget)
		self.domain_label.setGeometry(QtCore.QRect(20, 70, 151, 16))
		font = QtGui.QFont()
		font.setFamily("Calibri")
		font.setPointSize(12)
		font.setBold(False)
		font.setItalic(False)
		font.setWeight(50)
		self.domain_label.setFont(font)
		self.domain_label.setStyleSheet("QLabel {\n"
"font: 12pt  \"Calibri\";\n"
"border: none;\n"
"}")
		self.domain_label.setObjectName("domain_label")
		self.domain_text = QtWidgets.QLineEdit(self.centralwidget)
		self.domain_text.setEnabled(True)
		self.domain_text.setGeometry(QtCore.QRect(210, 70, 161, 20))
		self.domain_text.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
		self.domain_text.setAcceptDrops(False)
		self.domain_text.setStyleSheet("QLineEdit {\n"
"background: white;\n"
"border: None\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"background: rgb(225, 225, 225);\n"
"}")
		self.domain_text.setObjectName("domain_text")
		self.domain_btn = QtWidgets.QPushButton(self.centralwidget)
		self.domain_btn.setGeometry(QtCore.QRect(380, 70, 41, 20))
		self.domain_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(211, 211, 211);\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(219, 219, 219);\n"
"}")
		self.domain_btn.setObjectName("domain_btn")
		self.count_label = QtWidgets.QLabel(self.centralwidget)
		self.count_label.setGeometry(QtCore.QRect(20, 100, 141, 16))
		font = QtGui.QFont()
		font.setFamily("Calibri")
		font.setPointSize(12)
		font.setBold(False)
		font.setItalic(False)
		font.setWeight(50)
		self.count_label.setFont(font)
		self.count_label.setStyleSheet("QLabel {\n"
"font: 12pt  \"Calibri\";\n"
"border: none;\n"
"}")
		self.count_label.setObjectName("count_label")
		self.offset = QtWidgets.QLabel(self.centralwidget)
		self.offset.setGeometry(QtCore.QRect(20, 130, 91, 16))
		font = QtGui.QFont()
		font.setFamily("Calibri")
		font.setPointSize(12)
		font.setBold(False)
		font.setItalic(False)
		font.setWeight(50)
		self.offset.setFont(font)
		self.offset.setStyleSheet("QLabel {\n"
"font: 12pt  \"Calibri\";\n"
"border: none;\n"
"}")
		self.offset.setObjectName("offset")
		self.count_slider = QtWidgets.QSlider(self.centralwidget)
		self.count_slider.setGeometry(QtCore.QRect(210, 100, 161, 22))
		self.count_slider.setStyleSheet("QSlider {\n"
"border: none;\n"
"background: 0;\n"
"}")
		self.count_slider.setMinimum(1)
		self.count_slider.setMaximum(100)
		self.count_slider.setSingleStep(1)
		self.count_slider.setPageStep(10)
		self.count_slider.setTracking(True)
		self.count_slider.setOrientation(QtCore.Qt.Horizontal)
		self.count_slider.setInvertedControls(False)
		self.count_slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
		self.count_slider.setTickInterval(0)
		self.count_slider.setObjectName("count_slider")
		self.offset_slider = QtWidgets.QSlider(self.centralwidget)
		self.offset_slider.setGeometry(QtCore.QRect(210, 130, 161, 22))
		self.offset_slider.setStyleSheet("QSlider {\n"
"border: none;\n"
"background: 0;\n"
"}")
		self.offset_slider.setMaximum(1000)
		self.offset_slider.setSingleStep(10)
		self.offset_slider.setPageStep(100)
		self.offset_slider.setProperty("value", 0)
		self.offset_slider.setOrientation(QtCore.Qt.Horizontal)
		self.offset_slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
		self.offset_slider.setObjectName("offset_slider")
		self.count_int = QtWidgets.QLCDNumber(self.centralwidget)
		self.count_int.setGeometry(QtCore.QRect(380, 100, 41, 21))
		self.count_int.setStyleSheet("QLCDNumber {\n"
"background: silver;\n"
"border: none;\n"
"}")
		self.count_int.setFrameShape(QtWidgets.QFrame.Box)
		self.count_int.setFrameShadow(QtWidgets.QFrame.Plain)
		self.count_int.setDigitCount(4)
		self.count_int.setProperty("value", 1.0)
		self.count_int.setObjectName("count_int")
		self.offset_int = QtWidgets.QLCDNumber(self.centralwidget)
		self.offset_int.setGeometry(QtCore.QRect(380, 130, 40, 21))
		self.offset_int.setStyleSheet("QLCDNumber {\n"
"background: silver;\n"
"border: none;\n"
"}")
		self.offset_int.setFrameShape(QtWidgets.QFrame.Box)
		self.offset_int.setFrameShadow(QtWidgets.QFrame.Plain)
		self.offset_int.setDigitCount(4)
		self.offset_int.setObjectName("offset_int")
		self.download_btn = QtWidgets.QPushButton(self.centralwidget)
		self.download_btn.setEnabled(True)
		self.download_btn.setGeometry(QtCore.QRect(160, 190, 121, 21))
		self.download_btn.setStyleSheet("QPushButton {\n"
"background-color: rgb(211, 211, 211);\n"
"border: none;\n"
"font: 10pt \"MS Sans\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(219, 219, 219);\n"
"}")
		self.download_btn.setObjectName("download_btn")
		Main.setCentralWidget(self.centralwidget)
		self.menuBar = QtWidgets.QMenuBar(Main)
		self.menuBar.setEnabled(True)
		self.menuBar.setGeometry(QtCore.QRect(0, 0, 441, 21))
		self.menuBar.setDefaultUp(False)
		self.menuBar.setNativeMenuBar(True)
		self.menuBar.setObjectName("menuBar")
		self.menu = QtWidgets.QMenu(self.menuBar)
		self.menu.setTearOffEnabled(False)
		self.menu.setObjectName("menu")
		Main.setMenuBar(self.menuBar)
		self.AUTH = QtWidgets.QAction(Main)
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap(":/menu_icons/icons/auth.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.AUTH.setIcon(icon1)
		self.AUTH.setObjectName("AUTH")
		self.SETTINGS = QtWidgets.QAction(Main)
		icon2 = QtGui.QIcon()
		icon2.addPixmap(QtGui.QPixmap(":/menu_icons/icons/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.SETTINGS.setIcon(icon2)
		self.SETTINGS.setObjectName("SETTINGS")
		self.menu.addAction(self.AUTH)
		self.menu.addSeparator()
		self.menu.addAction(self.SETTINGS)
		self.menuBar.addAction(self.menu.menuAction())

		self.retranslateUi(Main)
		QtCore.QMetaObject.connectSlotsByName(Main)

	def retranslateUi(self, Main):
		_translate = QtCore.QCoreApplication.translate
		Main.setWindowTitle(_translate("Main", "VK Wall Loader"))
		self.manual_button.setText(_translate("Main", "Скачивание вручную"))
		self.auto_button.setText(_translate("Main", "Автоматическое скачивание"))
		self.domain_label.setToolTip(_translate("Main", "<html><head/><body><p>Домен - короткий идентификатор сообщества. Если url сообщества в адресной строке имеет такой вид: vk.com/sevenup228, то sevenup228 - это домен.</p></body></html>"))
		self.domain_label.setText(_translate("Main", "Домен сообщества:"))
		self.domain_btn.setText(_translate("Main", "..."))
		self.count_label.setText(_translate("Main", "Количество постов:"))
		self.offset.setToolTip(_translate("Main", "<html><head/><body><p>Количество постов, которое будет пропущено.</p></body></html>"))
		self.offset.setText(_translate("Main", "Смещение:"))
		self.download_btn.setText(_translate("Main", "Начать загрузку"))
		self.menu.setTitle(_translate("Main", "Меню"))
		self.AUTH.setText(_translate("Main", "Авторизация"))
		self.SETTINGS.setText(_translate("Main", "Настройки"))