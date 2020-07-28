from PyQt5 import QtWidgets, QtCore, QtGui
import threading
import vk_api
import sys
import os

from extra import config_handler, download
from gui import Auth, Design,Domain, ConfirmAuth, Settings


class Authorization(Auth.Ui_Authorization):

	def __init__(self, config):
		super().__init__()
		self.setupUi(self)

		self.config = config
		self.hide = True

		self.icons = [QtGui.QIcon(), QtGui.QIcon()]

		self.icons[1].addPixmap(QtGui.QPixmap(":/app_icons/icons/unvisib.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.icons[0].addPixmap(QtGui.QPixmap(":/app_icons/icons/visib.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

		self.confirm_window = ConfirmAuth.Ui_AuthWindow(vk_api)
		self.confirm_window.constructor()
		self.vk = None

		self.constructor()


	def constructor(self):
		self.login_line.setText(self.config.read("LOGIN"))
		self.password_line.setText(self.config.read("PASSWORD"))
		self.checktosave.setChecked(self.config.read("save"))

		self.password_line.setEchoMode(QtWidgets.QLineEdit.Password)
		self.show_password.clicked.connect(self.change_echomode)

		self.save_btn.clicked.connect(self.save_clicked)
		self.cancel_btn.clicked.connect(self.cancel_clicked)


	def save_clicked(self):
		login = self.login_line.text()
		password = self.password_line.text()

		if not (len(login) and len(password)):
			self.cancel_btn.clicked.emit()
		else:
			self.vk = self.confirm_window.get_vk_session(login, password)

		if self.vk:
			if self.checktosave.isChecked():
				self.config.write("LOGIN", login)
				self.config.write("PASSWORD", password)

			self.config.write("save", self.checktosave.isChecked())

			self.close()


	def cancel_clicked(self):
		self.login_line.setText(self.config.read("LOGIN"))
		self.password_line.setText(self.config.read("PASSWORD"))
		self.checktosave.setChecked(self.config.read("save"))

		if not self.hide:
			self.show_password.clicked.emit()

		self.close()


	def change_echomode(self):
		self.hide = not self.hide

		if self.hide:
			self.password_line.setEchoMode(QtWidgets.QLineEdit.Password)
		else:
			self.password_line.setEchoMode(QtWidgets.QLineEdit.Normal)

		self.show_password.setIcon(self.icons[self.hide])


	def Open(self):
		self.exec_()


class App(QtWidgets.QMainWindow, Design.Ui_Main):
	downloading_finished = QtCore.pyqtSignal()

	def __init__(self):
		# я сижу в темноте, 
		# и она не хуже в комнате, чем
		# темнота снаружи
		
		super().__init__()
		self.setupUi(self)

		self.list_of_widgets = [self.manual_button, self.auto_button,
								self.domain_text, self.domain_btn,
								self.count_slider, self.count_int,
								self.offset_slider, self.offset_int,
								self.download_btn]
		self.threads = []

		self.config = config_handler.Config(os.path.join(os.getcwd(), "config.json"))
		self.constructor()
		self.auth.Open()
		self.show()


	def constructor(self):
		#
		self.domain_window = Domain.Ui_Domain(self)
		self.domain_window.constructor()

		self.auth = Authorization(self.config)
		self.settings = Settings.Settings(self.config)

		self.downloader = download.Downloader(self)
		# instances


		self.turn_widgets(state=False, excepts=[self.manual_button, self.auto_button])
		self.manual_button.toggled.connect(self.method_toggled)
		self.auto_button.toggled.connect(self.method_toggled)

		self.domain_btn.clicked.connect(self.open_domain_window)

		self.count_slider.valueChanged.connect(lambda: self.count_int.display(self.count_slider.value()))
		self.offset_slider.valueChanged.connect(lambda: self.offset_int.display(self.offset_slider.value()))

		self.download_btn.clicked.connect(self.start_downloading)

		self.downloading_finished.connect(self.finish_downloading)

		self.AUTH.triggered.connect(self.auth.Open)
		self.SETTINGS.triggered.connect(self.settings.Open)
		#connections

		domain_data = self.config.read("domains")

		for k, v in domain_data.items():
			self.domain_window.addDomain(k, v)


	def closeEvent(self, e:QtCore.QEvent):
		print("Closing app...")
		self.config.close()
		e.accept()


	def open_domain_window(self):
		self.domain_window.Open()


	def start_downloading(self):
		count = self.count_int.intValue()
		offset = self.offset_int.intValue()

		if len(self.settings.path.text()):
			pth = self.settings.path.text()
		else:
			pth = None

		type_of_downloading = self.config.read("target_of_download")

		if self.manual_button.isChecked():
			domain = self.domain_text.text()

			if len(domain):
				print(f"[{self.start_downloading.__name__}] Preparing to download...")

				thread = threading.Thread(target=self.downloader.download, args=(
								self.auth.vk, 
								domain, count, 
								offset, pth, 
								type_of_downloading))

				self.turn_widgets(False)

				thread.start()
		else:
			print(f"[{self.start_downloading.__name__}] Preparing to download...")

			self.turn_widgets(False)
			domains = self.config.read("domains")

			for domain, _ in domains.items():
				self.threads.append(threading.Thread(target = self.downloader.download, args=(
								self.auth.vk, 
								domain, count, 
								offset, pth, 
								type_of_downloading)))
			
			for thread in self.threads:
				thread.start()


	def finish_downloading(self):
		if len(self.threads):
			for thread in self.threads:
				if thread.isAlive():
					return

		self.method_toggled()
		self.threads = []


	def method_toggled(self):
		if self.manual_button.isChecked():
			self.turn_widgets(True)
		elif self.auto_button.isChecked():
			self.turn_widgets(False)
			self.turn_widgets(True, excepts=[self.domain_text])


	def turn_widgets(self, state:bool = False, excepts:list = []):
		'''
		turns the widgets on this window on if state == True and off else
		widgets in the list of excepts will not be affected
		'''

		for widget in self.list_of_widgets:
			if widget in excepts:
				continue
			else:
				widget.setEnabled(state)



app = QtWidgets.QApplication(sys.argv)
window = App()
sys.exit(app.exec_())
