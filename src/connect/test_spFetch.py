import unittest
import spotipy
# import spprams
import src.connect.spprams as spprams
import src.connect.spFetch as spFetch

class TestspFetch(unittest.TestCase):

    global sp
    sp = spprams.sp

    def test_connection(self):
        # sp = spprams.sp
        congrats_uri = 'spotify:track:6kblAEj0T0312fv5QWsXzo'
        results = sp.track(congrats_uri, market="US")
        
        message = "Spotify either does not have a connection or credentials are missing or wrong"
        self.assertTrue(str(results).__contains__("Congratulations"), msg = message)

    def test_download(self):
        # sp = spprams.sp

        plist_uri = 'spotify:playlist:5btwrnSd9riqzzfLN6vfML'
        results = spFetch.downloadPlist(sp, plist_uri)

        message = "Spotify does not have proper authorization to do this"

        self.assertTrue(str(results).__contains__("I'm Leaving"), msg = message)

        

# Congratulations url https://open.spotify.com/track/6kblAEj0T0312fv5QWsXzo?si=c00f2d936ce54cac

# 15 Song plist https://open.spotify.com/playlist/4aYkj070xspLhgVdxCbxrF?si=962bc6df68374e2e

# 13 song plist https://open.spotify.com/playlist/5btwrnSd9riqzzfLN6vfML?si=2b5efbd32e4c4414

# 213 song plist https://open.spotify.com/playlist/4gXwZxo4lWpGoQmU3WD63g?si=e4da5a88f93740c8