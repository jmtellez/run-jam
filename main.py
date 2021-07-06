#imports
import billboard
from flask import Flask, jsonify, request
import requests
import json

#variables
spotify_URL = "https://api.spotify.com/v1/"
chart = billboard.ChartData('rock-songs')
config = json.load(open('config.json'))

app = Flask(__name__)

#helper functions
def return_headers(key:str)->str:
    value = request.headers[key]
    return value

def get_chart(chart_name:str):
    return chart_name

#endpoints
@app.route('/')
def index():
    #print(return_headers("test"))
    #print(get_chart('hot-100'))
    print(chart)
    #print(billboard.charts())
    return config["bearer_token"]

if __name__=="__main__":    
    app.run(debug=True)