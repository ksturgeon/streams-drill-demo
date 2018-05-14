from confluent_kafka import Producer
import json
import requests

#make a request to the weather dot gov api for Waxhaw, NC weather station
url = 'https://api.weather.gov/stations/KEQY/observations/current'

headers = {
        #just need any user-agent string
    'User-Agent': 'demo-application',
    'Cache-Control': 'no-cache'
    }

ok = True

while ok:
    response = requests.request('GET', url, headers=headers)

    response.encoding = 'json'
    #print(response.text)
    ok = response.status_code == requests.codes.ok

    p = Producer({'streams.producer.default.stream': '/demo-stream'})
    p.produce('topic1', response.text)
    p.flush()

    time.sleep(10)