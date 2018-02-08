from sqlitewrapper import *

db = Database('sites.db')

cmd = """
      CREATE TABLE pairs (
        uuid text,
        link text
      );
      """

db.command(cmd)

db.save()

db.close()

input('Finished...')

