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
def get_track_id(q:str, token:str):
    url = spotify_URL+'search/'
    params = {'q':q,'type':'track','limit':'1'}
    headers = {'Authorization':'Bearer {0}'.format(token)}
    response = requests.get(url,params=params,headers=headers)
    temp = response.json()
    try:
        return temp['tracks']['items'][0]['id']
    except:
        return None

def get_track_features(id:str, token:str):
    return "track features"

def get_header(key:str)->str:
    value = request.headers[key]
    return value

def get_chart_data(chart_name:str):
    local_chart_data = billboard.ChartData(chart_name)
    return local_chart_data

def temp_ids():
    return "IDS"

#endpoints
@app.route('/get-track-ids')
def get_track_IDs():
    #get all headers using helper
    chart_data_with_ids = [{}]
    #bearer_token = get_header('token')
    chart = get_header('chart')
    bpm = get_header('bpm')
    #get chart data  using helper
    chart_data = get_chart_data(chart)
    for song in chart_data:
        temp_song = {}
        temp_song['song'] = song.title
        temp_song['artist'] = song.artist
        temp_song['trackID'] = get_track_id(song.title, config['bearer_token'])
        chart_data_with_ids.append(temp_song)
        #print(get_track_id(song.title, config['bearer_token']))#,bearer_token))
    print(chart_data_with_ids)
    return "emanuelzapata"

@app.route('/get-tracks')
def get_tracks():
    #get all headers using helper
    bearer_token = get_header('token')
    chart = get_header('chart')
    bpm = get_header('bpm')
    #get chart data  using helper
    chart_data = get_chart_data(chart)
    print(get_track_id("q","token"))
    return bearer_token + chart + bpm

@app.route('/')
def index():
    return config["bearer_token"]

if __name__=="__main__":    
    app.run(debug=True)