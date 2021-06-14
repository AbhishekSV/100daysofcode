from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
import pprint
import os

timeline = input("Which year do you want to travel to? Enter the date in YYYY-MM-DD format: ")
year = timeline.split('-')[0]

response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{timeline}")
soup = BeautifulSoup(response.text, 'html.parser')

all_songs = soup.find_all(name='span', class_='chart-element__information__song')
all_artists = soup.find_all(name='span', class_='chart-element__information__artist')
song_dict = {}

for i in range(0,len(all_songs)):
    song_dict[i] = [all_songs[i].getText(), all_artists[i].getText()]
# pprint.pprint(song_dict)
# spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
spotify = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=os.environ.get('SPOTIPY_REDIRECT_URI'),
        client_id=os.environ.get('SPOTIPY_CLIENT_ID'),
        client_secret=os.environ.get('SPOTIPY_CLIENT_SECRET'),
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = spotify.current_user()["id"]
# print(user_id)
# result = spotify.search(q=f"artist:'coldplay' track:'yellow' year:2000", type="track")
# print(result['tracks']['items'][0]['uri'])

song_uris = []
for (key,value) in song_dict.items():
    result = spotify.search(q=f"artist:{value[1]} track:{value[0]}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{value[0]} doesn't exist in Spotify. Skipped.")

playlist = spotify.user_playlist_create(user=user_id, name=f"{timeline} Billboard 100", public=False)
# print(playlist)
spotify.playlist_add_items(playlist_id=playlist["id"], items=song_uris)