#imports
import billboard
from flask import Flask, jsonify, request
from flask_restx import Resource, Api
import requests
import json
import time

#Variables
spotify_URL = "https://api.spotify.com/v1/"
config = json.load(open('config.json')) #will probably be removed later
chart_data = None

#helper functions
def jsonify_chart_data(chart_data):
    temp_chart_data = []
    for song in chart_data:
        temp_song = {}
        temp_song['song'] = song.title
        temp_song['artist'] = song.artist
        temp_chart_data.append(temp_song)
    return temp_chart_data          

def get_all_track_ids(chart_data, bearer_token):
    url = spotify_URL+"search/"
    for index, song in enumerate(chart_data):
        params = {'q':song['song'],'type':'track','limit':'1'}
        headers = {'Authorization':'Bearer {}'.format(bearer_token)}
        response = requests.get(url,params=params,headers=headers)
        results = response.json()
        try:
            chart_data[index].update({'trackID':results['tracks']['items'][0]['id']})
        except:
            del chart_data[index]
    return chart_data

def generate_track_ids_query_string(chart_data):
    ids = ""
    for song in chart_data:
        ids = ids + song['trackID'] + ","
    return ids

def get_add_track_features(trackIDS, bearer_token, chart_data):
    url = spotify_URL+'audio-features'
    params = {'ids':trackIDS}
    headers = {'Authorization':'Bearer {0}'.format(bearer_token)}
    response = requests.get(url,params=params, headers=headers)
    features = response.json()
    for index, feature in enumerate(features['audio_features']):
        chart_data[index].update(feature)
    return chart_data

#endpoints
app = Flask(__name__)
api = Api(app)

@api.route('/generate-playlist')
class Run_Jam(Resource):
    def get(self):
        #get all headers
        bearer_token = request.headers['bearer_token']
        chart_name = request.headers['chart']
        bpm = request.headers['bpm']
        user_ID = request.headers['user_ID']
        #get chart data
        chart_data = billboard.ChartData(chart_name)
        chart_data = jsonify_chart_data(chart_data)
        chart_data = get_all_track_ids(chart_data, bearer_token)
        chart_data = get_add_track_features(generate_track_ids_query_string(chart_data),bearer_token,chart_data)
        return chart_data



if __name__=="__main__":    
    app.run(debug=True)