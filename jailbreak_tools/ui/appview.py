import os
import re
import sys
import pathlib
from PyQt5 import QtWidgets, QtCore, QtGui
from . import ui_utils
from .. import CONFIG, PATHS, LOGGER, __title__, __version__


class AppView(QtWidgets.QWidget):
    sig_show = QtCore.pyqtSignal()
    sig_hide = QtCore.pyqtSignal()

    def __init__(self, app, name):
        super().__init__()
        self.app = app
        self.name = name
        ui_file = os.path.join(PATHS["qt"], '{}.ui'.format(self.name))
        ui_utils.load_ui(ui_file, self)
        self.setWindowTitle(__title__)
        self.setWindowIcon(ui_utils.get_icon("icon"))
        self.sig_show.connect(self.show)
        self.sig_hide.connect(self.hide)

    def showEvent(self, evt=None):
        ui_utils.show_ui(self)
        if evt:
            evt.accept()
