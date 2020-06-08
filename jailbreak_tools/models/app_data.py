import os
import re
from pprint import pprint as pp
from dataclasses import dataclass, field
from pathlib import Path
from .. import CONFIG, LOGGER, PATHS, __title__



@dataclass
class AppData:
    app_name: str = ""
    bundle_id: str = ""

    def __init__(self):
        super().__init__()

