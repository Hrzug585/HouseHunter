import requests
import json

base_path = 'http://localhost'
port = 8080
path = '/home'
id = 1234


def send_data(payload):
    json_payload = {
        "id": 123,
        "url": payload
    }
    requests.post(base_path + ":" + str(port) + path, json=json_payload)

