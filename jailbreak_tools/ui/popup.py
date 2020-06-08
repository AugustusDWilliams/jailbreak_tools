import os
import pathlib
from PyQt5 import QtWidgets, QtCore
from . import ui_utils
from .ui_constants import MsgBtns, MsgIcons
from .. import __title__, __version__, PATHS


class Popup(QtWidgets.QMessageBox):
    name = pathlib.Path(__file__).stem
    sig_execute = QtCore.pyqtSignal(str)

    def __init__(self, ui):
        super().__init__(ui)
        self.setWindowTitle(__title__)
        self.load()

    def load(self):
        self.connect_signals()

    def connect_signals(self):
        self.sig_execute.connect(self.execute)

    def execute(self, msg):
        self.setText(msg)
        return self.exec()

    def prompt(self, msg, icon=True):
        if icon:
            self.setIcon(MsgIcons.NOICON)
        self.setStandardButtons(MsgBtns.OK)
        return self.execute(msg)

    def warning(self, msg, icon=True):
        if icon:
            self.setIcon(MsgIcons.WARNING)
        self.setStandardButtons(MsgBtns.OK)
        return self.execute(msg)

    def error(self, msg, icon=True):
        if icon:
            self.setIcon(MsgIcons.CRITICAL)
        self.setStandardButtons(MsgBtns.OK)
        return self.execute(msg)

    def confirmation(self, msg, icon=True):
        if icon:
            self.setIcon(MsgIcons.QUESTION)
        self.setStandardButtons(MsgBtns.YES | MsgBtns.NO)
        return self.execute(msg)

    def save(self, msg, icon=True):
        if icon:
            self.setIcon(MsgIcons.QUESTION)
        self.setStandardButtons(MsgBtns.SAVE | MsgBtns.CANCEL)
        return self.execute(msg)

