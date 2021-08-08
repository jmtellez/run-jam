#imports
import billboard
from flask import Flask, jsonify, request
import requests
import json
import time

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

def get_header(key:str)->str:
    value = request.headers[key]
    return value

def get_chart_data(chart_name:str):
    local_chart_data = billboard.ChartData(chart_name)
    return local_chart_data

def create_trackID_list(tracks):
    ids = ""
    for track in tracks:
        ids = ids + track['trackID'] + ","
    return ids

def get_track_features(id:str, token:str):
    if id == None:
        return None
    else:
        url = spotify_URL+'audio-features'
        params = {'ids':id}
        headers = {'Authorization':'Bearer {0}'.format(token)}
        response = requests.get(url,params=params,headers=headers)
        temp = response.json()
        return temp

def filter_tracks(bpm:str, tracks):
    results = []
    for track in tracks:
        if track['tempo']>=float(bpm) and track['energy'] >= .50:
            results.append(track)
    return results

def create_and_populate_playlist(bpm:str, bearer_token:str, userID:str, tracks):
    body = {"name":"{0} BPM Playlist".format(bpm),"description":"Playlist Generated from Run-Jam","public":"false"}
    headers = {"Authorization":"Bearer {0}".format(bearer_token)}
    url = spotify_URL+"users/{0}/playlists"
    url = url.format(userID)
    response = requests.post(url,json=body,headers=headers)
    print(response.text)
    return str(response.status_code)

#endpoints
""" @app.route('/create-playlist')
def create_playlist():
    #https://api.spotify.com/v1/users/{user_id}/playlists
    body = {"name":"postman2","description":"described through postman","public":"false"}
    headers = {'Authorization':'Bearer {0}'.format(config['bearer_token'])}
    url = spotify_URL+'users/{0}/playlists'
    url = str.format(url,"1246353086")
    response = requests.post(url,json=body,headers=headers)
    responseJSON=response.json
    print(response.text)
    return str(response.status_code)
 """
@app.route('/get-track-ids')
def get_track_IDs():
    #get all headers using helper
    chart_data_with_ids = []
    #bearer_token = get_header('token')
    bearer_token = config['bearer_token']
    chart = get_header('chart')
    bpm = get_header('bpm')
    #userID = get_header('userID')
    userID = "1246353086"
    #get chart data  using helper
    chart_data = get_chart_data(chart)
    for song in chart_data:
        temp_song = {}
        temp_song['song'] = song.title
        temp_song['artist'] = song.artist
        temp_song['trackID'] = get_track_id(song.title, bearer_token)
        chart_data_with_ids.append(temp_song)
    chart_data_with_ids = [song for song in chart_data_with_ids if not (song['trackID'] == None)]
    trackIDS = create_trackID_list(chart_data_with_ids)
    features = get_track_features(trackIDS, bearer_token)
    #merge results
    for index, feature in enumerate(features['audio_features']):
        chart_data_with_ids[index].update(feature)
    chart_data_with_ids = filter_tracks(bpm,chart_data_with_ids)
    return json.dumps(chart_data_with_ids)

@app.route('/')
def index():
    return config["bearer_token"]

if __name__=="__main__":    
    app.run(debug=True)