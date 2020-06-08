import os
import re
import sys
import pathlib
from PyQt5 import QtWidgets, QtCore, QtGui
from . import ui_utils, AppView
from .. import CONFIG, PATHS, LOGGER, DB, __title__, __version__
from ..models import BumpTestModel
from ..constants import Messages


class ZeroAmbientCorrection(AppView):
    sig_add_tech_initials = QtCore.pyqtSignal(list)
    sig_set_date = QtCore.pyqtSignal(object)
    sig_add_gas_types = QtCore.pyqtSignal(list)
    sig_add_gas_serial_numbers = QtCore.pyqtSignal(list)
    sig_set_gas_conc = QtCore.pyqtSignal(str)
    sig_set_ppm_reading = QtCore.pyqtSignal(str)
    sig_set_test_passed = QtCore.pyqtSignal(str)

    def __init__(self, app, name):
        super().__init__(app, name)
        self.data = BumpTestModel()
        #self.load()

# ---------------------Load Functions------------------------------------
    def load(self):
        self.connect_signals()
        self.connect_widgets()
        self.load_tech_initials()
        self.load_gas_types()
        self.sig_set_date.emit(self.data.curr_date)

    def connect_signals(self):
        self.sig_show.connect(self.show)
        self.sig_hide.connect(self.hide)
        self.sig_add_tech_initials.connect(self.cb_tech_initials.addItems)
        self.sig_add_gas_types.connect(self.cb_gas_types.addItems)
        self.sig_add_gas_serial_numbers.connect(self.cb_gas_sn.addItems)
        self.sig_set_date.connect(self.input_date.setDate)
        self.sig_set_test_passed.connect(self.input_test_passed.setText)
        self.sig_set_gas_conc.connect(self.input_gas_conc.setText)

    def connect_widgets(self):
        self.cb_gas_types.currentTextChanged.connect(self.update_gas_type)
        self.cb_tech_initials.currentTextChanged.connect(self.update_tech_initials)
        self.cb_gas_sn.currentTextChanged.connect(self.update_gas_sn)
        self.input_ppm.textChanged.connect(self.update_ppm)
        self.input_module_sn.textChanged.connect(self.update_module_sn)
        self.btn_submit.clicked.connect(self.upload_data)

    def load_tech_initials(self):
        tech_initials = DB.get_tech_initials()
        self.sig_add_tech_initials.emit(tech_initials)

    def load_gas_types(self):
        gas_types = CONFIG.get("gas_types")
        self.sig_add_gas_types.emit(gas_types)

    def load_gas_conc(self):
        self.load_gas_sources()
        self.load_gas_sn()
        self.update_gas_sn()
        self.sig_set_gas_conc.emit(str(self.data.gas_conc))
        self.update_test_passed()

    def load_gas_sources(self):
        self.data.gas_sources = {}
        for gas in self.data.gas_type_list:
            active_gases = DB.get_gas_sources(gas)
            for row in active_gases:
                gas_id = row[5]
                gas_conc = row[3]
                titration_date = row[8]
                if gas_id not in self.data.gas_sources:
                    self.data.gas_sources[gas_id] = {"gas_conc": gas_conc, "titration_date": titration_date}
                else:
                    if self.data.gas_sources[gas_id]["titration_date"] < titration_date:
                        self.data.gas_sources[gas_id] = {"gas_conc": gas_conc, "titration_date": titration_date}

    def load_gas_sn(self):
        gas_serial_numbers = list(self.data.gas_sources.keys())
        self.sig_add_gas_serial_numbers.emit(gas_serial_numbers)

# --------------------Update Functions------------------------------------
    def update_tech_initials(self, tech_initials):
        self.data.tech_initials = tech_initials

    def update_gas_type(self, gas_type):
        self.data.gas_type = gas_type
        self.load_gas_conc()

    def update_gas_sn(self):
        self.data.gas_sn = self.cb_gas_sn.currentText()

    def update_module_sn(self, module_sn):
        self.data.module_sn = module_sn

    def update_ppm(self, ppm):
        self.data.ppm = ppm
        self.update_test_passed()

    def update_test_passed(self):
        self.sig_set_test_passed.emit(self.data.pass_fail)

    def upload_data(self):
        upload_error = self.data.check_params()
        if upload_error:
            self.app.popup.error(upload_error.msg)
        else:
            try:
                data = self.data.get_params()
                #TODO: Upload Data
            except Exception as err:
                LOGGER.error(err)
                self.app.popup.error(err.msg)
            else:
                print(data)
                #self.app.popup.prompt(Messages.BUMPTEST_UPLOADED)
                #self.sig_clear_sensor_sn.emit()
                #TODO: Clear input fields