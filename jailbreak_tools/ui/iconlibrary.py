import os
import re
import sys
import pathlib
from PyQt5 import QtWidgets, QtCore, QtGui
from . import ui_utils, AppView
from .. import CONFIG, PATHS, LOGGER, __title__, __version__


class IconLibrary(AppView):
    sig_add_comport = QtCore.pyqtSignal(QtWidgets.QListWidgetItem)
    sig_clear_comports = QtCore.pyqtSignal()

    def __init__(self, app, name):
        super().__init__(app, name)
        #self.load()

    def load(self):
        self.connect_signals()
        self.btn_scan.clicked.connect(self.get_comports)
        self.btn_submit.clicked.connect(self.delete_comports)

    def connect_signals(self):
        self.sig_add_comport.connect(self.list_comports.addItem)
        self.sig_clear_comports.connect(self.list_comports.clear)

    def get_comports(self):
        self.data.comports.clear()
        self.sig_clear_comports.emit()
        self.data.comports = core.scan_comports()
        self.add_comports()

    def add_comports(self):
        for port in self.data.comports.keys():
            item = QtWidgets.QListWidgetItem(port)
            item.setTextAlignment(QtCore.Qt.AlignHCenter)
            self.sig_add_comport.emit(item)

    def delete_comports(self):
        self.data.selected_comports = []
        for item in self.list_comports.selectedItems():
            self.data.selected_comports.append(self.data.comports[item.text()])
        core.remove_comports(self.data.selected_comports)
        QtCore.QTimer.singleShot(1000, self.get_comports)
        #TODO: Add to messages class
        #self.app.popup.prompt('Selected Comports Deleted.')