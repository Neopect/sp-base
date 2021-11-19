# Smart-Playlist app (AKA data_runner)

# from . import config
import os.path
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import random

plist_org = []
plist_sec = []
plist_act = []
plist_mas = []
global sp
userTrackLim = 50
usersExists = None
   


def downloadPlist(pid, name, path):
    # Creates the random playlists
    print("Downloading playlist info...")
    global plist_org
    global sp

    # done = False
    ofs = 0
    plist_temp = []

    while True:

        playlist_id = 'spotify:playlist:' + pid
        results = sp.playlist_tracks(playlist_id,fields="items(track(name,artists(name),id,href)),total", offset=ofs, market="US")
        

        

        print("Adding tracks to memory...")
        dummy_def = ['default-gen']
        dummy_def2 = ['default-mood']
        for x in range(len(results['items'])):
            plist_temp.append([results['items'][x]['track']['name'], results['items'][x]['track']['artists'][0]['name'], results['items'][x]['track']['id'], dummy_def, dummy_def2])

        if results['total'] > ofs:
            ofs += 100
        else:
            pathPlist = os.path.join(path, 'plists')
            os.mkdir(pathPlist)
            os.chdir(pathPlist)
            # fileDir = None
            
            fw = open("playlist_dl_"+name+".json", "w")
            # fw = open("plists/playlist_org_"+name+"_part_"+str(int(ofs/100))+".json", "w")
            fw.write(json.dumps(plist_temp, indent=4))
            fw.close()
            break

    # TODO Move this somewhere else vv
    # random.shuffle(plist_temp)
    # plist_org.append(plist_temp)

    return plist_temp



def downloadLiked(sp):
    pass


def downloadConf(spI, path, updated = False, globs = True, users = True):
    '''
    Download mass of playlists -
    - Parameters input: (str, bool, bool, bool)
    '''
    global sp 
    sp = spI
    testlist = downloadPlist('3PGHzE2Tqab3V5xH6JyVcW', 'glob', path)
    jsonList = json.dumps(testlist, indent=4)
    #print(jsonList)
    


def org():
    # Download the playlist tracks to json
    for x, val in enumerate(config.gPlayl):
        print("Opening universal playlists...")
        downloadPlist(val, 'uni_'+ str(x))
        

    for x, val in enumerate(config.playl):
        print("Opening personal playlists...")
        downloadPlist(val, 'per_'+ str(x))

    plist_sec = plist_org
    # plist_act = plist_org

    # Creates a 3 day master track
    z = 0
    while z < 3:
        plist_act.append(plist_sec[0][z*userTrackLim:z*userTrackLim+userTrackLim]) # Appends global playlist
        for x in range(len(config.users)):
            plist_act.append(plist_sec[x+1][z*userTrackLim:z*userTrackLim+userTrackLim]) # Appends part of user plist based day
            print()
            
        random.shuffle(plist_act)
        plist_mas.append([plist_act])

        plist_act =[]
        z += 1
        

    print(plist_org)

def create(usersOn):
    global plist_sec
    global plist_act
    global plist_mas
    global sp

    plistN = ''

    plist_sec = plist_org
    plist_act.append(plist_sec[0][:userTrackLim]) # Appends global playlist
    for x in range(len(usersOn)):
        if usersOn[x] == True:
            plist_act.append(plist_sec[x+1][:userTrackLim]) # Appends part of user plist based day
    random.shuffle(plist_act)
    plist_mas.append([plist_act])

    sp.user_playlist_create(config.spCred[0], "Work-Auto", description="Auto gen work playlist")
    playlists = sp.user_playlists(config.spCred[0])
    for playlist in playlists['items']:
        print(playlist['name'])
        if playlist['name'] == "Work-Auto":
            plistN = playlist['name']
    
    length = len(plist_act)
    seps = length / 100 + 1

    z = 0
    while z < seps:
        sp.playlist_add_items(config.spCred[0], )
        # plist_act.append(plist_sec[0][z*userTrackLim:z*userTrackLim+userTrackLim]) # Appends global playlist
        # for x in range(len(config.users)):
        #     plist_act.append(plist_sec[x+1][z*userTrackLim:z*userTrackLim+userTrackLim]) # Appends part of user plist based day
        #     print()
