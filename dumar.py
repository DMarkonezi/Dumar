import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

#from html.parser import HTMLParser
import yt_dlp

# For reading the CLIENT_ID and CLIENT_SECRET from .env file on local machine
from dotenv import load_dotenv

# Reads from .env file and creates the env. vars
load_dotenv()

CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
REDIRECT_URI = 'http://127.0.0.1:8888/callback'

if not CLIENT_ID or not CLIENT_SECRET:
    raise ValueError("Missing CLIENT_ID or CLIENT_SECRET in environment variables")

# TEST public playlist
playlist_url = "https://www.youtube.com/playlist?list=PLoV7WC9F3gOdyQZzj-jFMaP-WdlVsfTUC"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope="user-library-read playlist-modify-public"
))

if __name__ == "__main__":

    ydl_opts = {
        'quiet': True,
        'extract_flat': True # Gets only the metadata (titles, duration...) and doesn't download them
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:

        youtube_playlist_song_info = ydl.extract_info(playlist_url, download=False)

        for song_info in youtube_playlist_song_info['entries']:
            print(song_info['title'])

    playlist_name = "Test" 

    # Finds the user with id, for now its only ours
    user_id = sp.me()['id'] 

    # Creating playlist

    new_playlist = sp.user_playlist_create(
        user=user_id,
        name=playlist_name,
        public=True,
        collaborative=False,
        description="Enjoy your new playlist created by Dumar"
    )

    # Adding tracks
    for song in youtube_playlist_song_info['entries']:\

        song_title = song['title']
        song_author = song['uploader']

        search_query = f"track:{song_title}"

        search_result = sp.search(
            q=search_query,
            type='track',
            limit=1
        )

        if search_result['tracks']['items']:
            track_uri = search_result['tracks']['items'][0]['uri']

            sp.playlist_add_items(playlist_id=new_playlist['id'], items=[track_uri])
        else:
            print("There is no such track on spotify!")




