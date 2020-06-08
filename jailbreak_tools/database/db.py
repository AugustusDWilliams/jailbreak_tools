import dataset
from pathlib import Path
from .. import CONFIG, LOGGER
from ..exceptions import DatabaseConnectionError, DatabaseNotConnected, BaselineTableNotPresent
from . import queries


class Database(dataset.Database):
    def __init__(self):
        if CONFIG.get("database"):
            self.connect_to_db()
            self.table = self[CONFIG.get("table_name")]

    def connect_to_db(self):
        try:
            db_path = CONFIG.get("database")
            url = f"sqlite:///{db_path}"
            super().__init__(url)
            #self.connect()
        except Exception as err:
            LOGGER.error(err)

    def set_db_path(self, db_path):
        try:
            self.db_path = Path(db_path)
            self.db_exists = self.db_path.exists()
            if self.db_exists:
                self.name = self.db_path.name
            else:
                self.name = None
                raise DatabaseConnectionError
        except:
            self.name = ""
            self.db_path = ""
            self.db_exists = False

    def get_bundle_id(self, app):
        res = self.table.find_one(App=app)
        return res["BundleID"]

DB = Database()