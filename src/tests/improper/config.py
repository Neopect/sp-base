import sys
import os
import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sys.path.insert(0, 'src/conf')
sys.path.insert(0, 'src/fetch')

import spFetch as fetch
import configRW as conf

# Create paths
root = None
rootConfig = None
root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../")
rootConfig = os.path.join(root, "../configure")
rootPlists = os.path.join(rootConfig, "plists")
os.chdir(root)

print(root)
print(rootConfig)

scopes = ['user-library-read', 'playlist-read-private']


def fetchSP(scoper):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scoper))
    return sp

# Download liked songs
# fetch.downloadLiked(fetchSP(scopes[0]), rootConfig)

# Run config
# conf.configRunner(root, rootConfig)

# Fetch downloads
# fetch.downloadConf(fetchSP(scopes[1]), rootPlists)


def download(sp, pid):
    results = sp.playlist_tracks(pid)
    print(json.dumps(results, indent=4))


download(fetchSP(scopes[1]), '6V5grGhvcAyNoBWvoct1wF')
