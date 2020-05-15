#!/usr/bin/env python
import os
from dotenv import load_dotenv
load_dotenv()
from config import CONFIG
from logger import LOGGER


def get_function():
    sshpass = os.getenv("SSHPASS")
    ssh_flag = os.getenv("SSH_FLAG")
    pwd = os.getenv("SSH_PASSWORD")
    cmd = os.getenv("CMD")
    flag = os.getenv("FLAG")
    ipaddress = os.getenv("IPADDRESS")
    user = os.getenv("USERNAME")
    app_theme_folder = os.getenv("APP_THEME_FOLDER")
    phone_theme_folder = os.getenv("PHONE_THEME_FOLDER")
    func = "{} {} \"{}\" {} {} {} {}@{}:{}".format(
        sshpass, ssh_flag, pwd, cmd, flag, app_theme_folder, user, ipaddress,  phone_theme_folder)
    return func


if __name__ == "__main__":
    func = get_function()
    print(func)
    LOGGER.info("Theme Uploaded")
