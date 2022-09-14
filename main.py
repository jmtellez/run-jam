#imports
from flask import Flask, jsonify, request, Response
from dotenv import load_dotenv
from controllers.Health import Health
from util.Billboard import Billboard
from util.Spotify import Spotify
load_dotenv()
import json
health = Health()

chartFile = open("assets/chart-list.json")
availableChartsList = json.load(chartFile)

app = Flask(__name__)

@app.route('/ping')
def ping():
    return Response(health.ping())

@app.route('/deepPing')
def deepPing():
    return Response(health.deepPing())

@app.route('/getAvailableCharts')
def getAvailableCharts():
    return Response(json.dumps(availableChartsList))

@app.route('/test')
def test():
    billboard = Billboard('greatest-hot-100-singles')
    return Response(json.dumps(billboard.get_chart_data()))

if __name__ == '__main__':
    spotify = Spotify()
    spotify.get_access_token()
    spotify.search_for_song()
    app.run(debug=True)