from uuid import uuid3, NAMESPACE_DNS
from flask import Flask, redirect
from sqlitewrapper import *

app = Flask(__name__)

db = Database('sites.db')

@app.route('/')
def index():
  return '''URL or Code: <input type="text" id="url" /><button onclick="window.location=document.getElementById(\'url\').value
  .replace(\'https\', \'\')
  .replace(\'http\', \'\')
  .replace(\'://\', \'\')
  \">Submit</button>'''

@app.route('/<path:text>')
def convert(text=''):
  if text != 'favicon.ico':
    if '.' in text:
      db.command('SELECT * FROM "pairs" WHERE link = "{link}";'.format(link=text))
      selected = db.fetch()
      if len(selected) > 0:
        selected = selected[0]
        if len(selected) > 0:
          selected = selected[0]
          print('Pulled from database')
          print('Code: {}'.format(selected))
          return selected
      unique = str(uuid3(NAMESPACE_DNS, text))
      code = unique[0:3] + unique[-3:]
      db.command('INSERT INTO "pairs" VALUES ("{id}", "{link}");'.format(id=code, link=text))
      db.save()
      print('Generated new code')
      print('Code: {}'.format(code))
      return code
    else:
      db.command('SELECT * FROM "pairs" WHERE uuid = "{uuid}";'.format(uuid=text))
      selected = db.fetch()
      if len(selected) > 0:
        selected = selected[0]
        if len(selected) > 0:
          selected = selected[1]
          print('Pulled from database')
          return redirect('http://{}'.format(selected))
      else:
        return 'Invalid Code!'
  else:
    return ''

if __name__ == "__main__":
	app.run(host='0.0.0.0')
