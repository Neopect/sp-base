import os.path
import json
import sys
# sys.path.insert(0, 'src/conf')
# import configRW as config

def show_tracks(results, pid):
    # Complies results into the proper format as a python list

        plist_temp = []
        for item in results['items']:
            track = item['track']
            plist_temp.append([track['name'], 
                            track['artists'][0]['name'], 
                            track['duration_ms'], 
                            track['explicit'], 
                            track['id'],
                            track['preview_url'],
                            'default-gen,', 
                            'default-mood,',
                            pid])
        return plist_temp



def downloadPlist(sp, pid):
    # Creates the random playlists

    plist_temp = []
    ofs = 0
    
    while True:
        print("Downloading playlist info...")
        results = sp.playlist_tracks(pid,
                                    offset=ofs,
                                    fields='playlist_id,fields="items(track(name,artists(name),duration_ms,explicit,id,preview_url)),total',
                                    market="US")
        
        if len(results['items']) == 0: # If no more items in list, then stop
            break
        
        print("Adding tracks to memory...")
        plist_temp = plist_temp + show_tracks(results, pid)

        ofs = ofs + len(results['items'])

    return plist_temp



def downloadLiked(sp, path):
    # Downloads liked playlist

    plist_temp = []
    
    results = sp.current_user_saved_tracks()
    plist_temp = plist_temp + show_tracks(results)

    while results['next']: # Repeats requests until no more tracks left
        results = sp.next(results)
        plist_temp = plist_temp + show_tracks(results)

    os.chdir(path)
    with open("playlist_dl_liked.json", "w") as fw:
        fw.write(json.dumps(plist_temp, indent=4))

