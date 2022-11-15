import requests
import json
from requests.auth import HTTPBasicAuth


def test_auth_1c():
    # uath = {"login": "pypbot", "password": "pypbot!"}
    basic = HTTPBasicAuth('pypbot', 'pypbot')
    data = {"PhoneNumber": "+380502108663"}
    response = requests.post('http://95.217.227.88:8486/ApiSmileFoodTest/hs/ForReff/CheckUser',
                             data=json.dumps(data),
                             auth=basic)
    # response = requests.post('http://95.217.227.88:8486/ApiSmileFoodTest/hs/ForReff/CheckUser',
    # auth=('pypbot', 'pypbot'))
    print(response.status_code)
    print(response.text)


def test_auth_ref():
    body = {"login": "+380631634797", "password": "9T8cez8n533PRRJm"}
    headers = {"Content-Type": "application/json; charset=utf-8"}
    response = requests.post('https://api.smilefooder.com.ua/api/v1/login', headers=headers, json=body)
    print(response.status_code)
    # print(response.text)
    print(response.json())
