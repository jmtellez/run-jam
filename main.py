import billboard
from flask import Flask, jsonify, request
import requests

spotifyURL = "https://api.spotify.com/v1/"
chart = billboard.ChartData('hot-100')

app = Flask(__name__)
@app.route('/get-tracks')
def get_tracks():    
    #Get BPM parameter
    bpm = request.args.get('bpm')
    #Get Header key
    #Get Top Tracks
    #Start the querying of spotify API
    #parse results
    #return results
    return bpm
@app.route('/')
def index():
    url = spotifyURL+'search/'
    headers = {'Authorization':'Bearer BQDW4TGVeIYTuql1wJPI2iXOqK-Fg4ttQcZktbAYxKwI34sizaqZZ2h_FeaSOA96aWH2M95X9gYfbcfeXQNkFAJ5WuVk7SG-AdM4erSpcd5sVDJ3DvYwba-2PKeW_19qOmrHKS99-eafkv8jzuTt6yAxRZu0JFB5QGeDrlO17jBzFHq8nkvy6PpxmYzY7D1SEYgqeH62SdSBp7t_x38Gbfc_h4BgWSfqRm-9KZjr5--L2kfxNqzqVl4lpzOLuenpZrpROjlOlNS4uDLfwUVb'}
    params = {'q':'taylor swift enchanted','type':'track','limit':'1'}
    response = requests.get(url, params=params, headers=headers)
    temp = response.json()
    #print(temp["tracks"]["items"]["id"])
    #this will get the first track result which should be the proper track if searching by artist AND song name
    print(temp['tracks']['items'][0]['id'])
    return response.json()

@app.route('/hot-100')
def return_hot_100():
    return chart[0].title

@app.route('/headers')
def return_headers():
    head = request.headers["test"]
    #return "Request  Headers: \n" + str(headers)
    return head
def main():
    for song in chart:
        print(song.title)

if __name__=="__main__":
    main() 
    app.run(debug=True)