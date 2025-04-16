import os

from html.parser import HTMLParser
import yt_dlp

# For reading the CLIENT_ID and CLIENT_SECRET from .env file on local machine
from dotenv import load_dotenv

import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Reading from .env file
load_dotenv()

CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
REDIRECT_URI = 'http://127.0.0.1:8888/callback'

if not CLIENT_ID or not CLIENT_SECRET:
    raise ValueError("Missing CLIENT_ID or CLIENT_SECRET in environment variables")


url = "https://www.youtube.com/watch?v=HA9-354DM2E&ab_channel=SvetlanaCecaRaznatovic"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope="user-library-read playlist-modify-public"
))

if __name__ == "__main__":

    with yt_dlp.YoutubeDL() as ydl:
        youtube_video_info = ydl.extract_info(url, download=False)
        youtube_video_title = youtube_video_info['title']

    print(youtube_video_title)

    playlists = sp.current_user_playlists()
    print("Playlists:", playlists)