import os
import shutil
import anyconfig
from pathlib import Path, PurePath
from . import PATHS



class Config:
    name = None

    def __init__(self):
        self.config_file = os.path.join(
            PATHS.app_data_config, "{}.yaml".format(os.getenv("ENV").lower()))
        self.default_file = os.path.join(
            PATHS['default_config'], "{}.yaml".format(os.getenv("ENV").lower()))
        self._data = dict()
        self.check_if_config_file_exists()
        self.load()

    def check_if_config_file_exists(self):
        if not os.path.exists(PATHS.app_data_config):
            self.create_config_dir()
        if not os.path.exists(self.config_file):
            self.create_config_file()

    def create_config_dir(self):
        os.mkdir(PATHS.app_data_config)

    def create_config_file(self):
        shutil.copy(self.default_file, self.config_file)

    def load(self):
        self._data = anyconfig.load(
            [self.default_file, self.config_file])

    def save(self):
        anyconfig.dump(self._data, self.config_file)

    def get(self, item):
        return self._data[item]

    def set(self, key, value):
        self._data[key] = value
        self.save()

    def __getitem__(self, item):
        return self._data[item]

    def __setitem__(self, key, value):
        self._data[key] = value
        self.save()

CONFIG = Config()
