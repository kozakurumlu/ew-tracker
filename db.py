import sqlite3
from datetime import datetime

class Database:
    def __init__(self, db_file):
        self.db_file = db_file
        self.create_table()

    def create_table(self):
        with sqlite3.connect(self.db_file) as db:
            cursor = db.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS ew (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    task TEXT NOT NULL,
                    subject TEXT NOT NULL,
                    beak TEXT NOT NULL,
                    due_date DATE NOT NULL
                )
            """)
            db.commit()

    def get_ews(self):
        """
        Retrieve all EWs from the database.
        """
        with sqlite3.connect(self.db_file) as db:
            cursor = db.cursor()
            cursor.execute("SELECT id, task, subject, beak, due_date FROM ew")
            return cursor.fetchall()

    def create_ew(self, task, subject, beak, due_date):
        """
        Create a new EW task in the database.
        """
        with sqlite3.connect(self.db_file) as db:
            cursor = db.cursor()
            cursor.execute("""
                INSERT INTO ew (task, subject, beak, due_date)
                VALUES (?, ?, ?, ?)
            """, (task, subject, beak, due_date))
            db.commit()
            return cursor.lastrowid

    # EXTRA CREDIT
    def get_ew(self, id):
        """
        Retrieve a specific EW from the database by ID.
        """
        with sqlite3.connect(self.db_file) as db:
            cursor = db.cursor()
            cursor.execute("SELECT id, task, subject, beak, due_date FROM ew WHERE id = ?", (id,))
            return cursor.fetchone()