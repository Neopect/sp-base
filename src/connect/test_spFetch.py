import unittest
import src.connect.spprams as spprams
import src.connect.spFetch as spFetch

class TestspFetch(unittest.TestCase):

    global sp
    sp = spprams.sp

    def test_connection(self):
        
        congrats_uri = 'spotify:track:6kblAEj0T0312fv5QWsXzo'
        results = sp.track(congrats_uri, market="US")
        
        message = "Spotify either does not have a connection or credentials are missing or wrong"
        self.assertTrue(str(results).__contains__("Congratulations"), msg = message)

    def test_download(self):

        plist_uris = ['spotify:playlist:5btwrnSd9riqzzfLN6vfML', 'spotify:playlist:4gXwZxo4lWpGoQmU3WD63g', 'spotify:playlist:2YothbbzcjcLnGX46WqHuT']

        results = spFetch.downloadPlist(sp, plist_uris[0])
        message = "Spotify does not have proper authorization to do this"
        self.assertTrue(str(results).__contains__("I'm Leaving"), msg = message)

        results = spFetch.downloadPlist(sp, plist_uris[1])
        message = "Spotify was not able to get the remaining tracks from the playlist"
        print(results)
        self.assertTrue(str(results).__contains__("The Wanderer"), msg = message)

        

# Congratulations url https://open.spotify.com/track/6kblAEj0T0312fv5QWsXzo?si=c00f2d936ce54cac

# 15 Song plist https://open.spotify.com/playlist/4aYkj070xspLhgVdxCbxrF?si=962bc6df68374e2e

# 13 song plist https://open.spotify.com/playlist/5btwrnSd9riqzzfLN6vfML?si=2b5efbd32e4c4414

# 213 song plist https://open.spotify.com/playlist/4gXwZxo4lWpGoQmU3WD63g?si=e4da5a88f93740c8

# 149 song plist https://open.spotify.com/playlist/2YothbbzcjcLnGX46WqHuT?si=4bc726b042014e80