from flask import Flask, request
from flask_ngrok import run_with_ngrok
from KoBert import *


app = Flask(__name__)
run_with_ngrok(app)
@app.route('/')

def home():
     return "Hello Flask!"

@app.route('/sentiment')
def sentiment():
  txt = request.args.get('txt')
  kb = KoBert()
  res = kb.sentimental(txt)
  print(res)
  return res

if __name__ == '__main__':
     app.run()
