import sqlite3


class SQLiteDatabaseReader:
    def __init__(self, db_file):
        self.db_file = db_file
        self.connection = None

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.db_file)
            return True
        except sqlite3.Error as e:
            print(f"Error connecting to the database: {e}")
            return False

    def execute_query(self, query):
        if not self.connection:
            print("Database connection is not established. Please call connect() first.")
            return None

        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except sqlite3.Error as e:
            print(f"Error executing SQL query: {e}")
            return None

    def close(self):
        if self.connection:
            self.connection.close()
