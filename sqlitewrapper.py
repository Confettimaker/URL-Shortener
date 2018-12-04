import sqlite3 as sql3

class Database(object):
    def __init__(self, database):
        self.connection = sql3.connect(database, check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.result = self.cursor.fetchall()

    def close(self):
        self.connection.close()

    def save(self):
        self.connection.commit()

    def command(self, command):
        self.cursor.execute(command)
        self.result = self.cursor.fetchall()

    def fetch(self):
        return self.result
