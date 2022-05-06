# This will be for modifying and uploading playlists

# TODO
# - Create playlist
# - Modify playlist


def get_pid_from_plist(uri):
    # Credit to @plamere 
    split_uri = uri.split(':')
    if len(split_uri) == 5:
        return split_uri[4]
    elif len(split_uri) == 3:
        return split_uri[2]
    else:
        return None



def randomizePlist():
    # Randomize playlist within spotify
    pass


def createPlist(sp, plist, name, des):
    
    print("Creating playlist...")

    user_id = sp.me()['id']
    results = sp.user_playlist_create(user_id, name, True, True, description=des)

    # Grab the uri for the new playlist
    puri = results['uri']
    print("Your new playlist id is " + puri)
    
    # Add songs to playlist
    uris = []
    for track in plist:
        uris.append('spotify:track:' + track[4])
    
    sp.playlist_add_items(puri, uris)

    return puri



def updatePlist(sp, pid, songs_added, songs_removed):
    # Update playlist with new songs and remove old ones
    # TODO Ensure length is proper
    # TODO Looking into user_playlist_replace

    uri_r, uri_a = []
    user_id = sp.me()['id']

    for srem in songs_removed:
        uri_r.append('spotify:track:' + srem)
        sp.playlist_remove_all_occurrences_of_items(pid, uri_r)

    for sadd in songs_added:
        uri_a.append('spotify:track:' + sadd)
        sp.playlist_add_items(pid, uri_a)

    print('Updated playlist')


