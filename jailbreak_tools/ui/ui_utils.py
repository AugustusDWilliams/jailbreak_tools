import os
from PyQt5 import QtWidgets, QtCore, QtGui, uic
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt
from .ui_constants import *
from .. import PATHS, __title__



def load_ui(ui_file, base_instance=None):
    return uic.loadUi(ui_file, base_instance)


def get_initial_size():
    desktop = QtWidgets.QDesktopWidget()
    screen = desktop.cursor().pos()
    dims = desktop.screenGeometry(screen)
    return QtCore.QSize(dims.width() / 2, dims.height())


def show_ui(widget, secondary=False):
    desktop = QtWidgets.QDesktopWidget()
    num_screens = desktop.screenCount()
    screen_num = 0
    if secondary and num_screens > 0:
        screen_num = 1
    screen = desktop.screenGeometry(screen_num)
    frame = widget.frameGeometry()
    frame.moveCenter(screen.center())
    widget.move(frame.topLeft())
    widget.setWindowIcon(get_icon("icon")) #Automatically set all widget's icon


def get_icon(img, pixmap=False):
    path = os.path.join(PATHS["imgs"], '{}.gif'.format(img))
    if pixmap:
        return QtGui.QPixmap(path)
    return QtGui.QIcon(path)


def set_icon(widget, img, pixmap=False):
    icon = get_icon(img, pixmap)
    widget.setIcon(icon)


def popup(ui, text="", icon=MsgIcons.NOICON, buttons=QtWidgets.QMessageBox.Ok, modal=QtCore.Qt.NonModal):
    msg_box = QtWidgets.QMessageBox(ui)
    msg_box.setWindowTitle(__title__)
    msg_box.setWindowIcon(get_icon("icon"))
    msg_box.setText(text)
    msg_box.setStandardButtons(buttons)
    msg_box.setIcon(icon)
    msg_box.setWindowModality(modal)
    msg_box.exec()


def get_filename(ui=None, initial_dir='', is_save=True, file_filter='', is_dir=False):
    options = QtWidgets.QFileDialog.Options()
    options |= QtWidgets.QFileDialog.DontUseNativeDialog
    options |= QtWidgets.QFileDialog.DontUseCustomDirectoryIcons
    dialog = QtWidgets.QFileDialog()
    dialog.setOptions(options)
    dialog.setNameFilter(file_filter)
    # ARE WE TALKING ABOUT FILES OR FOLDERS
    if is_dir:
        dialog.setFileMode(QtWidgets.QFileDialog.DirectoryOnly)
    else:
        dialog.setFileMode(QtWidgets.QFileDialog.AnyFile)
    # OPENING OR SAVING
    if is_save:
        dialog.setAcceptMode(QtWidgets.QFileDialog.AcceptSave)
    else:
        dialog.setAcceptMode(QtWidgets.QFileDialog.AcceptOpen)
    if initial_dir != "":
        dialog.setDirectory(initial_dir)
    else:
        dialog.setDirectory(os.path.expanduser('~/Desktop'))
    #path = dialog.getSaveFileName(ui, "datalogger.csv")[0]
    #return path
    if dialog.exec_() == QtWidgets.QDialog.Accepted:
        path = dialog.selectedFiles()[0]
        return path
    else:
        return ''

def confirmation_prompt(msg="Are You Sure?", btns=QMessageBox.Yes | QMessageBox.No, icon=QMessageBox.Warning, modal=Qt.NonModal):
    prompt = QMessageBox()
    prompt.setWindowTitle(__title__)
    prompt.setWindowIcon(get_icon("icon"))
    prompt.setText(msg)
    prompt.setStandardButtons(btns)
    prompt.setIcon(icon)
    prompt.setWindowModality(modal)
    return prompt

def closeEvent(evt=None):
    msg = "Are you sure you wish to exit the program?"
    prompt = confirmation_prompt(msg)
    confirm = prompt.exec()
    if confirm == QMessageBox.Yes and evt:
        evt.accept()
    else:
        evt.ignore()