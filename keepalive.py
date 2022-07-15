#to keep our bot alive even when the program closes

from flask import Flask
from threading import Thread

app=Flask('')

@app.route('/')
def hello():
  return 'Hello! Alive'

def run():
  app.run(host='0.0.0.0',port=8080)

def keepAlive():
  t=Thread(target=run)
  t.start()
