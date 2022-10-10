#https://www.youtube.com/watch?v=tMH16T74fWE
#thanks brain for this idea

from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
  return "jalapeno bot is online"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()
