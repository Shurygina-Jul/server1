from flask import Flask, request
from datetime import datetime
import time


server_start = datetime.now()
app = Flask(__name__)
messages = [
    {"username": "Jack", "text": "Hello everyone!", "timelamp": time.time()},
     {"username": "Jack2", "text": "Hello Jack!", "timelamp": time.time()}]

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
    print(request.json)
    username = "Jack"
    text = "Hello"
    messages.append({"username": username, "text": text, "timelamp": time.time()})
    return {'ok': True}

@app.route("/get_messages")
def get_messages():
    return {'messages': messages}



app.run()