#imports
import billboard
from flask import Flask, jsonify, request
import requests
import json

#variables
spotify_URL = "https://api.spotify.com/v1/"
config = json.load(open('config.json'))
chart_data = None

app = Flask(__name__)

#helper functions
def get_header(key:str)->str:
    value = request.headers[key]
    return value

def get_chart_data(chart_name:str):
    local_chart_data = billboard.ChartData(chart_name)
    return local_chart_data

#endpoints
@app.route('/get-tracks')
def get_tracks():
    #get all headers using helper
    bearer_token = get_header('token')
    chart = get_header('chart')
    bpm = get_header('bpm')
    #get chart data  using helper
    chart_data = get_chart_data(chart)
    
    print(chart_data)
    return bearer_token + chart + bpm

@app.route('/')
def index():
    return config["bearer_token"]

if __name__=="__main__":    
    app.run(debug=True)