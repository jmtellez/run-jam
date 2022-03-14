import json
from urllib import request
import requests

class Spotify:
    def __init__(self):
        self.url = "https://api.spotify.com/v1/"
    
    def get_track(self, song, artist, bearer_token):
        q = '{song} {artist}'.format(song=song, artist=artist)
        Authorization = 'Bearer {bearer_token}'.format(bearer_token=bearer_token)
        params = {'q':q,'type':'track','limit':'1'}
        headers = {'Authorization':Authorization}
        response = requests.get(self.url+"search", params=params, headers=headers)
        track = json.loads(response.content)
        return track
    
    def get_track_analysis(self, track_id, bearer_token):
        Authorization = 'Bearer {bearer_token}'.format(bearer_token=bearer_token)
        headers = {'Authorization':Authorization}
        audio_analysis_url = "{url}audio-analysis/{track_id}".format(url=self.url,track_id=track_id)
        response = requests.get(audio_analysis_url,headers=headers)
        track = json.loads(response.content)
        return track