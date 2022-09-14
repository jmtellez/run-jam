import requests
from dotenv import load_dotenv
load_dotenv()
import os
import base64

class Spotify:
    bearer_token = "BQC2EsXj8MU_Hfn9oUtRX-qL_q-K36psSmThogKFDDkttnWIxgmup88dzYcynyt1Jeba0Kr1HdyOC5aGEcaM48gWe1kfJieOz6aOfF5R3YWK3kM5k6Hw2iS7GQXe9Rx_KczGIZ0_dK6XOl56BUL8pO5ZryB8MlXilYRTyNi87KA"
    def __generate_base64_token(self, CLIENT_ID, CLIENT_SECRET):
        message = f"{CLIENT_ID}:{CLIENT_SECRET}"
        messageBytes = message.encode('ascii')
        base64bytes = base64.b64encode(messageBytes)
        base64Message = base64bytes.decode('ascii')
        return base64Message

    def get_access_token(self):
        spotify_token_url = os.environ.get("SPOTIFY_TOKEN_URL")
        base64_message = self.__generate_base64_token(os.environ.get("CLIENT_ID"),os.environ.get("CLIENT_SECRET"))
        response = requests.post(
            spotify_token_url,
            data={"grant_type":"client_credentials"},
            headers={"Authorization":"Basic {base64_message}".format(base64_message=base64_message)}
            )
        return response.json()['access_token']
    
    def search_for_song(self, song):
        spotify_search_url = os.environ.get("SPOTIFY_SEARCH_URL")
        access_token = self.get_access_token()
        response = requests.get(
            spotify_search_url,
            headers={"Authorization":"Bearer {bearer_token}".format(bearer_token=access_token)},
            params={"q":"track:{title}: artist:{artist}".format(title=song['title'], artist=song['artist']),"type":"track","limit":1}
        )
        return response
        # print(response.json())
    
    def filter_song_list(self, song_list):
        filtered_list = []
        for song in song_list:
            if song['tracks']['total']!=0:
                filtered_list.append(song)
        return filtered_list