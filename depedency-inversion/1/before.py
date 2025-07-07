import logging

logging.basicConfig(level=logging.INFO)


class MysqlDatabase:
    def connect(self):
        logging.info("Connecting to MySQL database...")

    def disconnect(self):
        logging.info("Disconnecting from MySQL database...")


class BudgetReport:
    def __init__(self, db: MysqlDatabase):
        self.db = db

    def generate(self):
        self.db.connect()
        logging.info("Generating budget report...")
        self.db.disconnect()


db = MysqlDatabase()
report = BudgetReport(db)
report.generate()
