import sqlite3 as sql
from datetime import date

connection = sql.connect('sites.db')
cursor = connection.cursor()

cmd = """
      CREATE TABLE pairs (
        uuid text,
        link text
      );
      """

cursor.execute(cmd)

connection.commit() #save

connection.close()

input('Finished...')
