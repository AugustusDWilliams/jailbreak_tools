import os
import re
from pathlib import Path
from pprint import pprint as pp
from . import CONFIG, LOGGER, PATHS, DB


def get_files(src, filter_files=False, filter_dir=False):
    files = [file for file in Path(src).iterdir()]
    if filter_files:
        files = [file for file in files if not file.is_dir()]
    elif filter_dir:
        files = [file for file in files if file.is_dir()]
    return files

def get_themes():
    theme_root = CONFIG.get("theme_folder")
    theme_paths = get_files(theme_root, filter_dir=True)
    return {theme.stem:theme for theme in theme_paths}

