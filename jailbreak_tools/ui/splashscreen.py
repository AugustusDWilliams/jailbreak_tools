import os
import pathlib
from PyQt5 import QtWidgets, QtCore
from . import ui_utils
from .. import __title__, __version__, PATHS



class SplashScreen(QtWidgets.QWidget):
    name = pathlib.Path(__file__).stem
    sig_show = QtCore.pyqtSignal()
    sig_hide = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        path = os.path.join(PATHS["qt"], "{}.ui".format(self.name))
        ui_utils.load_ui(path, self)
        self.setWindowTitle(__title__)
        self.setWindowIcon(ui_utils.get_icon("icon"))
        self.setWindowFlags(QtCore.Qt.SplashScreen)
        self.load()

    def load(self):
        self.connect_signals()

    def connect_signals(self):
        self.sig_show.connect(self.show)
        self.sig_hide.connect(self.hide)

    def showEvent(self, evt=None):
        ui_utils.show_ui(self)
        if evt:
            evt.accept()
