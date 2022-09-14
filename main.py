#imports
from flask import Flask, jsonify, request, Response
from dotenv import load_dotenv
from controllers.Health import Health
from controllers.RunJam import RunJam
from util.Billboard import Billboard
from util.Spotify import Spotify
load_dotenv()
import json
health = Health()
run_jam = RunJam()

chart_file = open("assets/chart-list.json")
available_chart_list = json.load(chart_file)

app = Flask(__name__)

@app.route('/ping')
def ping():
    return Response(health.ping())

@app.route('/deepPing')
def deepPing():
    return Response(health.deepPing())

@app.route('/getAvailableCharts')
def get_available_charts():
    return Response(json.dumps(available_chart_list))

@app.route('/getSongsList')
def get_songs_list():
    return Response(status=200)

@app.route('/createPlaylist')
def create_playlist():
    return Response(status=200)
    
@app.route('/getOneSong')
def TEST_get_one_song():
    spotify_song_list = []
    billboard = Billboard('hot-100')
    song_list = billboard.get_chart_data()
    # print(song_list[0])
    spotify = Spotify()
    spotify.get_access_token()
    song = spotify.search_for_song(song_list[0])
    for song in song_list:
        spotify_song_list.append(spotify.search_for_song(song).json())
    # print(spotify_song_list)
    filtered_song_list = spotify.filter_song_list(spotify_song_list)
    print(len(filtered_song_list))
    return Response(json.dumps(filtered_song_list))

    # return Response(json.dumps(song.json()))

if __name__ == '__main__':
    app.run(debug=True)