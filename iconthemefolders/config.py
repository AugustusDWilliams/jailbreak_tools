import os


class Config:

    def __init__(self):
        super().__init__()
        self._sshpass = "sshpass"
        self._ssh_flag = "-p"
        self._ssh_password = os.getenv("SSH_PASSWORD")
        self._cmd = "scp"
        self._flag = "-r"
        self._username = os.getenv("USERNAME") or "root"
        self._ipaddress = os.getenv("IPADDRESS")
        self._app_theme_folder = os.getenv("APP_THEME_FOLDER") or "/Appcon/IconLibrary/"
        self._phone_theme_folder = os.getenv("PHONE_THEME_FOLDER") or "/Library/Themes/"

    @property
    def sshpass(self):
        return self._sshpass


CONFIG = Config()
