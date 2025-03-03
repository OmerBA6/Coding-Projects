from bs4 import BeautifulSoup
import requests
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

BILLBOARD_URL = "https://www.billboard.com/charts/hot-100/"
SPOTIFY_CLIENT_ID = os.environ["SPOTIFY_CLIENT_ID"]
SPOTIFY_CLIENT_SECRET = os.environ["SPOTIFY_CLIENT_SECRET"]


# --------------------------------- Billboard Scraping ---------------------------------------------------- #
def billboard_scraping(date):

    response = requests.get(f"{BILLBOARD_URL}{date}/")
    response.raise_for_status()
    billboard_html = response.text
    soup = BeautifulSoup(billboard_html, "html.parser")

    li_tags = soup.find_all(name="li",
                            class_="o-chart-results-list__item // lrv-u-flex-grow-1 lrv-u-flex "
                                   "lrv-u-flex-direction-column lrv-u-justify-content-center lrv-u-border-b-1 "
                                   "u-border-b-0@mobile-max lrv-u-border-color-grey-light lrv-u-padding-l-050 "
                                   "lrv-u-padding-l-1@mobile-max")

    songs_names = []
    for li_tag in li_tags:
        songs_names.append(li_tag.find(name="h3", id="title-of-a-story").getText().strip())

    return songs_names
# -------------------------------------------------------------------------------------------------------- #


# --------------------------------- Spotify URI serach ---------------------------------------------------- #
def get_songs_uri(songs_names_list):
    uris = []
    for song_name in songs_names_list:
        result = sp.search(q=f"{song_name}", type="track")
        try:
            uri = result["tracks"]["items"][0]["uri"]
            uris.append(uri)
        except IndexError:
            print(f"{song_name} doesn't exist in Spotify. Skipped.")

    return uris
# -------------------------------------------------------------------------------------------------------- #


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                                               client_secret=SPOTIFY_CLIENT_SECRET,
                                               redirect_uri="http://localhost:8888/callback",
                                               scope="playlist-modify-private",
                                               cache_path="tokens.txt",
                                               show_dialog=True))

user_id = sp.current_user()["id"]

wanted_date = input("Which year would you like to travel to?"
                    " Type the date in this format YYYY-MM-DD: ")

songs_names_lists = billboard_scraping(wanted_date)
song_uris = get_songs_uri(songs_names_lists)

playlist_create_response = sp.user_playlist_create(user=user_id,
                                                   name=f"{wanted_date} Billboard 100",
                                                   public=False,
                                                   description=f"Top 100 songs from Bliiboard chart by the date {wanted_date}")

new_playlist_id = playlist_create_response['id']
sp.playlist_add_items(new_playlist_id, song_uris)





