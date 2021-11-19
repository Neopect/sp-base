# Smart-Playlist app (AKA data_runner)

# from . import config
import os.path
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import random
import sys

sys.path.insert(0, 'src/conf')

import configRW as config

plist_org = []
plist_sec = []
plist_act = []
plist_mas = []
global sp
userTrackLim = 50
usersExists = None
   


def downloadPlist(pid, name, path):
    # Creates the random playlists
    
    global plist_org
    global sp

    # done = False
    ofs = 0
    plist_temp = []

    while True:
        print("Downloading playlist info...")
        playlist_id = 'spotify:playlist:' + pid
        results = sp.playlist_tracks(playlist_id,fields="items(track(name,artists(name),id,href)),total", offset=ofs, market="US")
        
        print("Adding tracks to memory...")
        # for x in range(len(results['items'])):
        #     plist_temp.append([results['items'][x]['track']['name'], results['items'][x]['track']['artists'][0]['name'], results['items'][x]['track']['id'], ['default-gen'], ['default-mood']])
        # TODO Test implementation of this v
        for item in results['items']:
            track = item['track']
            plist_temp.append([track['name'], track['artists'][0]['name'], track['id'], ['default-gen'], ['default-mood']])


        if results['total'] > ofs:
            ofs += 100
        else:
            pathPlist = os.path.join(path, 'plists')
            if (os.path.isdir(pathPlist) == False):
                os.mkdir(pathPlist)
            os.chdir(pathPlist)
            # fileDir = None
            
            fw = open("playlist_dl_"+name+".json", "w")
            # fw = open("plists/playlist_org_"+name+"_part_"+str(int(ofs/100))+".json", "w")
            fw.write(json.dumps(plist_temp, indent=4))
            fw.close()
            break

    return plist_temp



def downloadLiked(sp, path):
    templist = []
    def show_tracks(results):
        for item in results['items']:
            track = item['track']
            # print([track['artists'][0]['name'], track['name']])
            # print([track['name'], track['artists'][0]['name'], track['id'], ['default-gen'], ['default-mood']])
            templist.append([track['name'], track['artists'][0]['name'], track['id'], ['default-gen'], ['default-mood']])

    results = sp.current_user_saved_tracks()
    show_tracks(results)

    while results['next']:
        results = sp.next(results)
        show_tracks(results)

    # File json gen
    pathPlist = os.path.join(path, 'plists')
    if (os.path.isdir(pathPlist) == False):
        os.mkdir(pathPlist)
    os.chdir(pathPlist)
    # fileDir = None
    
    fw = open("playlist_dl_liked.json", "w")
    # fw = open("plists/playlist_org_"+name+"_part_"+str(int(ofs/100))+".json", "w")
    fw.write(json.dumps(templist, indent=4))
    fw.close()


def downloadConf(spI, path, updated = False, globs = True, users = True):
    '''
    Download mass of playlists -
    - Parameters input: (str, bool, bool, bool)
    '''
    global sp 
    sp = spI

    if globs == True:
        for x, val in enumerate(config.gPlayl):
            print("Opening universal playlists...")
            downloadPlist(val, 'gobal_'+ str(x), path)

    if users == True:
        for x, val in enumerate(config.playl):
            print("Opening personal playlists...")
            downloadPlist(val, 'user_'+ str(x), path)
    
