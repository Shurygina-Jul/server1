import requests
username = input('Имя: ')
password= input('Введите пароль: ')
while True:
    text = input('Введите текст: ')
    requests.get('http://127.0.0.1:5000/sens_massage', json={'username': username, 'password': password, 'text': text})

