from flask import Flask
from datetime import datetime
import time

server_start = datetime.now()
app = Flask(__name__)

@app.route("/")
def hello():
    return 'Hello, User! Статус <a href= "/status"> смотреть здесь</a>'

@app.route("/status")
def status():
      return {'status': 'ok',
              'name': 'messenger',
              'server_start_time': server_start,
              'server_current_time': datetime.now(),
              'current_time_second': time.time()}

@app.route("/send_message")
def send_message():
    username = "Jack"
    text = "Hello"
    timelamp = time.time()



app.run()