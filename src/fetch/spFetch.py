import os.path
import json
import sys

sys.path.insert(0, 'src/conf')

import configRW as config
   

def downloadPlist(sp, pid, name, path):
    # Creates the random playlists
    
    ofs = 0
    plist_temp = []

    while True:
        print("Downloading playlist info...")
        playlist_id = 'spotify:playlist:' + pid
        results = sp.playlist_tracks(playlist_id,fields="items(track(name,artists(name),id,href)),total", offset=ofs, market="US")
        
        print("Adding tracks to memory...")
        for item in results['items']:
            track = item['track']
            plist_temp.append([track['name'], track['artists'][0]['name'], track['id'], ['default-gen'], ['default-mood']])

        # TODO See if possible to implement next feature from Liked songs
        if results['total'] > ofs:
            ofs += 100
        else:
            os.chdir(path)
            with open("playlist_dl_"+name+".json", "w") as fw:
                fw.write(json.dumps(plist_temp, indent=4))
            break

    return plist_temp



def downloadLiked(sp, path):
    plist_temp = []
    def show_tracks(results):
        for item in results['items']:
            track = item['track']
            plist_temp.append([track['name'], track['artists'][0]['name'], track['id'], ['default-gen'], ['default-mood']])

    results = sp.current_user_saved_tracks()
    show_tracks(results)

    while results['next']:
        results = sp.next(results)
        show_tracks(results)

    os.chdir(path)
    
    with open("playlist_dl_liked.json", "w") as fw:
        fw.write(json.dumps(plist_temp, indent=4))


def downloadConf(sp, path, updated = False, globs = True, users = True):
    '''
    Download mass of playlists -
    - Goes through each playlist in config and downloads it data with `downloadPlist`
    '''
    # global sp 
    # sp = spI

    if globs == True:
        for x, val in enumerate(config.gPlayl):
            print("Opening universal playlists...")
            downloadPlist(sp, val, 'gobal_'+ str(x), path)

    if users == True:
        for x, val in enumerate(config.playl):
            print("Opening personal playlists...")
            downloadPlist(sp, val, 'user_'+ str(x), path)
    
