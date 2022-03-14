#imports
from urllib import response
from flask import Flask, jsonify, request, Response
#from werkzeug import Response
from flask_restx import Resource, Api
import requests
import json
import time
from dotenv import load_dotenv
load_dotenv()
import os
from controllers.Billboard import Billboard
from controllers.Spotify import Spotify
from controllers.Utilities import Utilities
app = Flask(__name__)
billboard = Billboard()
spotify = Spotify()
utilities = Utilities()

@app.route('/')
def index():
    return Response({"'isHealthy':'True'"}, status=200)

@app.route('/preview_playlist')
def preview_playlist():
    # read in token, mile place and chart name from body
    # grab requested chart
    # make spotify calls to get all spotify track data
    # correlate mile pace to bpm in spotify
    # get song analysis from spotify
    # filter all songs with requested bpm from analysis array
    # return objects

    body = json.loads(request.data)
    bearer_token = body['bearer_token']
    mile_pace = body['mile_pace']
    chart_name = body['chart_name']
    chart = billboard.get_chart_data(chart_name=chart_name)
    spotify_chart = []
    for song in chart:
        spotify_chart.append(
            spotify.get_track(song=song['song'], artist=song['artist'], bearer_token=bearer_token)
        )
    spotify_analysis_chart = []
    for song in spotify_chart:
        try:
            temp = {}
            temp["id"]=song["tracks"]["items"][0]["id"]
            temp["analysis"] = spotify.get_track_analysis(song["tracks"]["items"][0]["id"], bearer_token=bearer_token)
            spotify_analysis_chart.append(temp)
        except:
            print("Failed to grab track ID")
    
    utilities.filter_song_list(mile_pace=mile_pace, spotify_analysis_chart=spotify_analysis_chart, spotify_chart=spotify_chart)
    return json.dumps(spotify_analysis_chart[0])#json.dumps(spotify_chart)    

@app.route('/test')
def test():
    billboard.get_chart_data('hot-100')
    
    spotify.get_track("good 4 u","Olivia Rodrigo","BQD9ma7WxtrzXipPUIJIpVfQbLzw__JtHlqkqH_dUQQeXvyGPlgEx4foycuQ8NwaWM1nldN8iCIdT3HTmGRKOxgr-bngtwJr3CRNv5tBRECDw4UMLhQTn6i138ygRMAL_SyKb2_XAl83YcRdhudZUTMBtq9M7A2g3Oqm2wzvfzkW4IC4CT4I26rRovslr84elVC5TVZuC-btsF3NLmvL_CrANolMWwDSAurfV613RaWH2xeDuh_tVU-XFug19FKEw38UlRuCJf-MeSaSgNDb")
    # data = json.loads(request.data)
    # print(data["firstName"])
    return "working"
if __name__ == '__main__': app.run(debug=True)