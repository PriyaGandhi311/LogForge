import logging
import sqlite3
from datetime import datetime

class SQLHandler(logging.Handler):
    def __init__(self, db_name='logs.db'):
        super().__init__()
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def emit(self, record):
        self.cursor.execute("INSERT INTO logs (timestamp, level, message, source) VALUES (?, ?, ?, ?)", (datetime.now().isoformat(), record.levelname, record.getMessage(), record.name) 
        )
        self.conn.commit()

logger = logging.getLogger("SystemLogger")
logger.setLevel(logging.INFO)
logger.addHandler(SQLHandler())


       
