from flask import Flask, request
from datetime import datetime
import time


server_start = datetime.now()
app = Flask(__name__)
messages = [
    {"username": "Jack", "text": "Hello everyone!", "timelamp": time.time()},
     {"username": "Jack2", "text": "Hello Jack!", "timelamp": time.time()}]
users = {'Jack':'12345', 'Jack2': '12345'}

@app.route("/")
def hello():
    return 'Hello, User! Статус <a href= "/status"> смотреть здесь</a>'

@app.route("/status")
def status():
      return {'status': 'ok',
              'name': 'messenger',
              'server_start_time': server_start,
              'server_current_time': datetime.now(),
              'current_time_second': time.time(),
              'users_count': len(users),
              'messages_count': len(messages)}

@app.route("/send_message")
def send_message():
    username = request.json['username']
    password = request.json['password']
    text = request.json['text']
    if username in users:
        if users[username]!= password:
            return {'ok': False}
    else:
        users[username] = password
    messages.append({"username": username, "text": text, "timelamp": time.time()})

    return {'ok': True}

@app.route("/get_messages")
def get_messages():
    after = float(request.args['after'])
    result = []
    for message in messages:
        if message['timelamp'] >after:
            result.append(message)
    return {'messages': result}



app.run()