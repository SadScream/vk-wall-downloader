# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Domain.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


try:
	from .InputDomain import Ui_InputDomain
except:
	from InputDomain import Ui_InputDomain


class InputWindow(Ui_InputDomain):

	def __init__(self, name:str = None, domain:str = None):
		super().__init__()
		self.setupUi(self)
		self.name:str = name
		self.domain:str = domain
		self.constructor()

	def constructor(self):
		self.group_name.setText(self.name)
		self.group_domain.setText(self.domain)
		self.ok_btn.clicked.connect(self.ok_close)
		self.cancel_btn.clicked.connect(self.close)

	def Open(self):
		return super().exec_()

	def ok_close(self):
		if not len(self.group_domain.text()):
			pass
		elif len(self.group_domain.text()) and not self.group_name.text():
			self.name = self.group_domain.text()
			self.domain = self.group_domain.text()
		else:
			self.name = self.group_name.text()
			self.domain = self.group_domain.text()

		self.close()

	def __str__(self):
		return f"InputWindow(name:{self.name}, id:{self.domain})"


class Input(QtWidgets.QLineEdit):

	def __init__(self, parent):
		super().__init__(parent)
		self.parent = parent

	def keyPressEvent(self, e):
		if e.key() == 13: # enter
			self.parent.confirm_domain.emit()
		else:
			e.accept()


class Ui_Domain(QtWidgets.QDialog):

	def __init__(self, main_window):
		self.window = main_window
		super().__init__()
		self.setupUi(self)


	def Open(self):
		self.setFocus()
		self.exec_()


	def keyPressEvent(self, event:QtCore.QEvent):
		if event.key() == 90 and event.modifiers() == QtCore.Qt.ControlModifier:
			self.domain_list.keyPressEvent(event)
		else:
			super().keyPressEvent(event)


	def constructor(self):
		self.accept_btn.clicked.connect(self.confirm)
		self.add_btn.clicked.connect(self.create_domain)


	def confirm(self):
		if self.domain_text.text() != "":
			self.window.domain_text.setText(self.domain_text.text())

		self.close()


	def create_domain(self):
		window = InputWindow()
		window.Open()

		if isinstance(window.name, str):
			if (len(window.name) and len(window.domain)):
				self.addDomain(window.domain, window.name)


	def addDomain(self, domain, name):
		self.domain_list.addDomain(name, domain)

		if hasattr(self.window, "config") and (domain not in self.window.config.read("domains")):
			self.window.config.write("domains", {domain: name})


	def deleteDomain(self, id_):
		for i, domain in enumerate(self.domain_list.getDomains()):
			if domain.id == domain:
				self.domain_list.deleteDomain(i)


	def getDomainByIndex(self, index):
		return str(self.domain_list.getDomainByIndex(index))


	def setupUi(self, Domain):
		Domain.setObjectName("Domain")
		Domain.resize(231, 241)
		Domain.setMinimumSize(QtCore.QSize(231, 241))
		Domain.setMaximumSize(QtCore.QSize(231, 241))
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(":/app_icons/icons/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		Domain.setWindowIcon(icon)
		Domain.setStyleSheet("QPushButton {\n"
"background-color:rgb(229, 229, 229);\n"
"border: none;\n"
"font: 12pt \"Calibri\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QDialog {\n"
"background-color:rgb(229, 229, 229);\n"
"}")
		self.domain_text = Input(Domain)
		self.domain_text.setGeometry(QtCore.QRect(10, 10, 141, 20))
		self.domain_text.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
		self.domain_text.setAcceptDrops(False)
		self.domain_text.setStyleSheet("QLineEdit {\n"
"border:None;\n"
"}")
		self.domain_text.setObjectName("domain_text")
		self.accept_btn = QtWidgets.QPushButton(Domain)
		self.accept_btn.setGeometry(QtCore.QRect(190, 10, 31, 20))
		self.accept_btn.setText("")
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap(":/app_icons/icons/passed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.accept_btn.setIcon(icon1)
		self.accept_btn.setIconSize(QtCore.QSize(26, 26))
		self.accept_btn.setObjectName("accept_btn")
		self.domain_list = List(Domain)
		self.domain_list.setGeometry(QtCore.QRect(10, 40, 211, 192))
		self.domain_list.setStyleSheet("QListView {\n"
"border:None;\n"
"}")
		self.domain_list.setObjectName("domain_list")
		self.add_btn = QtWidgets.QPushButton(Domain)
		self.add_btn.setGeometry(QtCore.QRect(160, 10, 31, 20))
		self.add_btn.setText("")
		icon2 = QtGui.QIcon()
		icon2.addPixmap(QtGui.QPixmap(":/app_icons/icons/w256h2561339405709Add1256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.add_btn.setIcon(icon2)
		self.add_btn.setIconSize(QtCore.QSize(20, 20))
		self.add_btn.setObjectName("add_btn")

		self.retranslateUi(Domain)
		QtCore.QMetaObject.connectSlotsByName(Domain)

	def retranslateUi(self, Domain):
		_translate = QtCore.QCoreApplication.translate
		Domain.setWindowTitle(_translate("Domain", "Domain"))


class List(QtWidgets.QListView):
	selectedDomain = None # last selected peer(discards when this window closing)
	removed = QtCore.pyqtSignal(int)
	rename = QtCore.pyqtSignal(int)
	rightClicked = QtCore.pyqtSignal(int, QtCore.QEvent)

	def __init__(self, parent:Ui_Domain):
		super().__init__(parent)

		self.parent = parent

		self.model:QtGui.QStandardItemModel = QtGui.QStandardItemModel()
		self.setModel(self.model)

		self.rename.connect(self.renameDomain)
		self.removed.connect(self.deleteDomain)
		self.rightClicked.connect(self._rightClicked)
		self.length = 0
		self.deleted_domain = None


	@QtCore.pyqtSlot(int, QtCore.QEvent)
	def _rightClicked(self, row:int, e:QtCore.QEvent):
		''' opens a context menu '''

		domain = self.getDomainByIndex(row)

		self.setSelection(self.rectForIndex(self.model.indexFromItem(domain)), QtCore.QItemSelectionModel.ClearAndSelect)
		domain.popMenu.exec_(self.mapToGlobal(e.pos()))


	def keyPressEvent(self, event:QtCore.QEvent):
		if event.key() == 90 and event.modifiers() == QtCore.Qt.ControlModifier:
			if self.deleted_domain:
				domain = self.deleted_domain
				self.addDomain(domain[1], domain[0], domain[2]) # addDomain(name, id_)  /  domain = (id_, name, indexAt)

				if hasattr(self.parent.window, "config"):
					self.parent.window.config.write("peers", (domain[2], (domain[0], domain[1])))

				self.deleted_domain = None
		else:
			event.ignore()


	def mousePressEvent(self, event:QtCore.QEvent):

		if event.type() == QtCore.QEvent.MouseButtonPress:
			if event.button() == QtCore.Qt.RightButton:
				pos = self.mapFromGlobal(QtGui.QCursor.pos())
				row = self.indexAt(pos).row() # returns -1 if there is no item at clicked point

				if row >= 0:
					self.rightClicked.emit(row, event)
			else:
				super().mousePressEvent(event)


	@QtCore.pyqtSlot(int)
	def renameDomain(self, index:int):
		domain:QtGui.QStandardItem = self.getDomainByIndex(index)

		change_domain_window = InputWindow(domain.name, domain.id)
		change_domain_window.Open()

		if hasattr(self.parent.window, "config"):
			self.parent.window.config.rewrite(name=domain.name, new_name=change_domain_window.name,
											id_=domain.id, new_id=change_domain_window.domain)

		domain.set_data(change_domain_window.name, change_domain_window.domain)
		self.parent.domain_text.setText(change_domain_window.domain)


	@QtCore.pyqtSlot(int)
	def deleteDomain(self, index:int):
		print(f"[{self.deleteDomain.__name__}] Deleting group\t", end='')

		domain = self.getDomains()[index]

		print(f"\"{domain.id}\":\t\"{domain.name}\"\t...", end="")

		self.model.removeRow(index)
		self.length -= 1

		if hasattr(self.parent.window, "config"):
			self.parent.window.config.remove("domains", domain.id)

		self.parent.domain_text.setText("")
		self.discardSelection()
		self.deleted_domain = (domain.id, domain.name, domain.indexAt)

		print("deleted!")


	def addDomain(self, name:str, id_:str, index:int = None):
		if isinstance(index, int):
			self.model.insertRow(index, DomainItem(self, name=name, id_=id_, indexAt=index))
		else:
			self.model.appendRow(DomainItem(self, name=name, id_=id_))
		
		self.length += 1
		
		if not isinstance(index, int):
			self.getDomains()[-1].getIndex()


	def getDomains(self) -> list:
		'''returns a list of PeerItem objects'''
		return [self.model.itemFromIndex(self.model.index(i, 0)) for i in range(self.length)]


	def getDomainByIndex(self, index):
		items = self.getDomains()

		if isinstance(index, int) and index <= self.length:
			return items[index]
		else:
			return None


	def selectionChanged(self, topLeft, bottomRight):
		'''срабатывает, когда пользователь выбирает какой-либо peer_id из списка'''

		if len(self.selectedIndexes()):
			range_ = QtCore.QItemSelectionRange(self.selectedIndexes()[0])
			self.selectedDomain = range_.bottom()
			self.changeTipedDomain()


	def changeTipedDomain(self):
		'''меняем значение поля с id на значение peer.id того объекта, по которому тыкнули'''

		self.parent.domain_text.setText(str(self.getDomainByIndex(self.selectedDomain)))


	def getSelectedDomain(self):
		'''возвращает выбранный объект DomainItem, если таковой имеет место быть'''

		if self.selectedDomain != None:
			return self.model.itemFromIndex(self.model.index(self.selectedDomain, 0))
		else:
			return None


	def discardSelection(self):
		'''reset selection value'''

		if self.selectedDomain != None:
			self.reset()
			self.selectedDomain = None


class DomainItem(QtGui.QStandardItem):
	'''
	:param view: an instance of List object
	:param name: a name of peer
	:param id_: an id of peer
	'''

	def __init__(self, view:List, name:str, id_:str, indexAt:int = None):
		super().__init__(name)

		self.view = view
		self.name = name
		self.id = str(id_)
		self.indexAt = indexAt

		self.setEditable(False)

		self.popMenu = QtWidgets.QMenu() # context menu
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(":/icons/icons/remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

		self.popMenu.addAction('Rename', lambda: self.view.rename.emit(self.row()))
		self.popMenu.addAction(icon, 'Remove', lambda: self.view.removed.emit(self.row()))


	def getIndex(self):
		if getattr(self, "indexAt", None) == None:
			self.indexAt = self.row()


	def set_data(self, name, id_):
		self.setText(name)
		self.name = name
		self.id = id_


	def __str__(self):
		return f"{self.id}"


if __name__ == '__main__':
	import sys
	import random
	import string
	import res_rc

	app = QtWidgets.QApplication(sys.argv)

	class Window(QtWidgets.QMainWindow):
		def __init__(self):
			super().__init__()
			self.setupUi(self)
			self.addicted()

		def addicted(self):
			domain = Ui_Domain(self)
			domain.constructor()
			domain.open()

			rands = [random.randint(100000, 10000000) for i in range(5)]

			for item in rands:
				domain.addDomain(item, ''.join([string.ascii_letters[random.randint(0, len(string.ascii_letters)-1)] for i in range(5)]))

		def setupUi(self, Main):
			Main.setObjectName("Main")
			Main.resize(100, 100)
			self.centralwidget = QtWidgets.QWidget(Main)
			self.centralwidget.setObjectName("centralwidget")
			Main.setCentralWidget(self.centralwidget)
			QtCore.QMetaObject.connectSlotsByName(Main)

	window = Window()
	sys.exit(app.exec_())
else:
	from . import res_rc