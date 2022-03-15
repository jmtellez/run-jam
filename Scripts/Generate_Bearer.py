from http import client
from dotenv import load_dotenv
import os
load_dotenv()
import requests
import json
import base64
from secrets import *

client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')
url = 'https://accounts.spotify.com/api/token'

message = f"{client_id}:{client_secret}"
messageBytes = message.encode('ascii')
base64bytes = base64.b64encode(messageBytes)
base64Message = base64bytes.decode('ascii')

headers = {}
data = {}
headers['Authorization'] = f"Basic {base64Message}"
data['grant_type'] = "client_credentials"
response = requests.post(url=url, headers=headers, data=data)

token = response.json()['access_token']
print(token)