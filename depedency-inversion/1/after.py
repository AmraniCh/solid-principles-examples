import logging
from abc import ABC

logging.basicConfig(level=logging.INFO)


class Database(ABC):
    def connect(self):
        raise NotImplementedError("Subclasses should implement this!")

    def disconnect(self):
        raise NotImplementedError("Subclasses should implement this!")


class MysqlDatabase(Database):
    def connect(self):
        logging.info("Connecting to MySQL database...")

    def disconnect(self):
        logging.info("Disconnecting from MySQL database...")


class BudgetReport:
    def __init__(self, db: Database):
        self.db = db

    def generate(self):
        self.db.connect()
        logging.info("Generating budget report...")
        self.db.disconnect()


db = MysqlDatabase()
report = BudgetReport(db)
report.generate()
