import sqlite3


class SQLiteDatabaseReader:
    def __init__(self, db_file):
        self.db_file = db_file
        self.connection = None

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.db_file)
        except sqlite3.Error as e:
            raise Exception(f"Error connecting to the database: {e}")

    def execute_query(self, query):
        if not self.connection:
            raise Exception("Database connection is not established. Please call connect() first.")

        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            names = list(map(lambda x: x[0], cursor.description))
            rows = cursor.fetchall()
            return names, rows
        except sqlite3.Error as e:
            raise Exception(f"Error executing SQL query: {e}")

    def close(self):
        if self.connection:
            self.connection.close()
