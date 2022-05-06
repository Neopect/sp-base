
def show_tracks(results):
    # Complies results into the proper format as a python list

        plist = []
        for item in results['items']:
            track = item['track']
            plist.append([
                            track['name'], 
                            track['artists'][0]['name'], 
                            track['duration_ms'], 
                            track['explicit'], 
                            track['id'],
                            track['preview_url'],
                            ['default-gen,'], 
                            ['default-mood,']
                            ])
        return plist



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
        plist_temp = plist_temp + show_tracks(results)


        ofs = ofs + len(results['items'])

    return plist_temp
