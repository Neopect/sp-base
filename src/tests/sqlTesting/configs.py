import sys
import os
# import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sys.path.insert(0, 'src/conf')
sys.path.insert(0, 'src/connect')

import spFetch as fetch
# import configRW as conf
import dbUsers as dbUser
import dbSongs as dbSongs


scopes = ['user-library-read', 'playlist-read-private']


def fetchSP(scoper):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scoper))
    return sp

# Download liked songs
# fetch.downloadLiked(fetchSP(scopes[0]), rootConfig)

# Fetch downloads
# fetch.downloadConf(fetchSP(scopes[1]), rootPlists)


def download(sp, pid):
    results = sp.playlist_tracks(pid)
    print(json.dumps(results, indent=4))


# download(fetchSP(scopes[1]), '6V5grGhvcAyNoBWvoct1wF')


# dbUser.addUser('Josph', '234kiasrf83')
# print(dbUser.returnUsers())
# print(dbSongs.listSongs())
# print(dbSongs.listPlist('2344oisdf'))

def testList1():
    dbUser.addUser('Tyler', '3Lyo7q26TJfwuH7JtvTAaO')
    print('User good')
    dbSongs.addPlist(fetch.downloadPlist(fetchSP(scopes[1]), '3Lyo7q26TJfwuH7JtvTAaO'), 'Tyler')

testList1()

# https://open.spotify.com/playlist/6V5grGhvcAyNoBWvoct1wF?si=
# https://open.spotify.com/playlist/3Lyo7q26TJfwuH7JtvTAaO?si=0a6380e4c36441d9