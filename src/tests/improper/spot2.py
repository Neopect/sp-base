import spotipy
from spotipy.oauth2 import SpotifyOAuth
import sys
import os

sys.path.insert(0, 'src/conf')
sys.path.insert(0, 'src/fetch')

import configRW as conf
import spFetch as fetch

scopes = ['user-library-read', 'playlist-read-private']

# Create paths
root = None
rootConfig = None
root = os.path.dirname(os.path.abspath(__file__))
rootConfig = os.path.join(root, "../../../configure")
rootPlists = os.path.join(rootConfig, "plists")
os.chdir(root)

def fetchSP(scoper):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scoper))
    return sp


# Download liked songs
# fetch.downloadLiked(fetchSP(scopes[0]), rootConfig)

# Run config
conf.configRunner(root, rootConfig)

# Fetch downloads
# fetch.downloadConf(fetchSP(scopes[1]), rootPlists)