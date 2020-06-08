import os
import pathlib
from . import __title__


class Paths:
    _data = dict()

    def __init__(self):
        self.root = pathlib.Path(os.path.realpath(__file__)).parent
        self.home = os.path.dirname(os.path.realpath(__file__))
        self.config_home = str(self.root / "config/default_config")
        self.devcon = str(self.root / ".data/devcon.exe")
        self.add_app_dirs()
        self.add_user_paths()
        self.check_for_app_data_dir()

    def add_app_dirs(self):
        for file in self.root.rglob("*"):
            if file.is_dir() and file.name != "__pycache__":
                setattr(self, file.name, str(file))
                self._data[file.name] = str(file)

    def add_user_paths(self):
        self.user_dir = os.path.expanduser("~")
        self.app_data_dir = os.path.join(self.user_dir, os.getenv("APP_DATA_DIR"), __title__)
        self.app_data_config = os.path.join(self.app_data_dir, "config")
        self.default_file_dir = os.path.join(self.app_data_dir, "data")
        self.safecide = os.path.join(self.user_dir, "SafeCide")
        self.docs_root = os.path.join(self.safecide, "Docs")

    def check_for_app_data_dir(self):
        if not os.path.isdir(self.app_data_dir):
            os.makedirs(self.app_data_dir)
        if not os.path.isdir(self.default_file_dir):
            os.makedirs(self.default_file_dir)

    def __getitem__(self, item):
        return self._data[item]


PATHS = Paths()
