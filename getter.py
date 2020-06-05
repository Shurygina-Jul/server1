import requests
import time
import datetime
last_timelamp = 0.0
while True:
    response = requests.get('http://127.0.0.1:5000/get_messages', params={'after': last_timelamp})
    messages = response.json()['messages']
    for massage in messages:
        dt = datetime.fromtimelamp(massage['timelamp'])
        dt = dt.strftime('%H:%M:%S %d/%m/%Y')
        print(massage['timelamp'], massage['usename'])
        print(massage)
        print()
        last_timelamp = massage['timelamp']


    time.sleep(1.0)
