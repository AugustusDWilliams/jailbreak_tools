import os
import sys
import re
import pathlib
from PyQt5 import QtWidgets, QtCore
from datetime import datetime, timedelta
from . import ui_utils
from .. import CONFIG, PATHS, LOGGER, __title__, __version__


class MainView(QtWidgets.QMainWindow):
    name = "app"
    sig_show = QtCore.pyqtSignal()
    sig_hide = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        ui_file = os.path.join(PATHS["qt"], "{}.ui".format(self.name))
        ui_utils.load_ui(ui_file, self)
        self.setWindowTitle("{} {}".format(__title__, __version__))
        self.setWindowIcon(ui_utils.get_icon("icon"))
        self.load()

    def load(self):
        self.connect_signals()

    def connect_signals(self):
        self.sig_show.connect(self.show)
        self.sig_hide.connect(self.hide)

    # ---------------------Show Functions------------------------------------
    def showEvent(self, evt=None):
        ui_utils.show_ui(self, secondary=False)
        if evt:
            evt.accept()

    # ---------------------Close Functions------------------------------------
    def closeEvent(self, evt=None):
        if os.getenv("ENV").upper() != "DEVELOPMENT":
            msg = "Are you sure you wish to exit the program?"
            prompt = ui_utils.confirmation_prompt(msg)
            confirm = prompt.exec()
            if confirm == QtWidgets.QMessageBox.Yes and evt:
                evt.accept()
            else:
                evt.ignore()
