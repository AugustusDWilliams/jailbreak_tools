import os
import re
import sys
import pathlib
from PyQt5 import QtWidgets, QtCore, QtGui
from . import ui_utils, AppView
from .. import CONFIG, PATHS, LOGGER, __title__, __version__


class Settings(AppView):
    sig_set_db_path = QtCore.pyqtSignal(str)


    def __init__(self, app, name):
        super().__init__(app, name)
        self.load()

    def load(self):
        self.connect_signals()

    def connect_signals(self):
        self.sig_show.connect(self.show)
        self.sig_hide.connect(self.hide)
        self.sig_set_db_path.connect(self.lbl_db_path.setText)
