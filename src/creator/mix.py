import random

def exceptions():
    pass

def randPlist(plists, tracklim = 50, globs = list(), globlim = 50):
    # Creates random playlist from set of users

    plist_final = []

    # Randomize each plist
    for x in range(len(plists)):
        random.shuffle(plists[x])
    random.shuffle(glob)

    # Take $tracklim out of each list at a time & $globlim from $glob
    # for ind, value in enumerate(plists):
    for x in range(len(plists)):
        try:
            plist_final.append(plists[x[:tracklim]])
        except:
            plist_final.append(plists[x])

    for x in range(len(globs)):
        try:
            plist_final.append(globs[x[:globlim]])
        except:
            plist_final.append(globs[x])

    # Check for full length,
    # TODO Later: fill in missing tracks with globs

    # Randomize and return
    random.shuffle(plist_final)
    return plist_final


# def mixComb():
#     pass

def dailyMix(plists, tracklim, glob, globlim, days, exceptions = False):
    # Creates a daily mix playlist for a set number of days
    
    

    pass

def dupCheck():
    pass


# def org():

#     # Creates a 3 day master track
#     z = 0
#     while z < 3:
#         plist_act.append(plist_sec[0][z*userTrackLim:z*userTrackLim+userTrackLim]) # Appends global playlist
#         for x in range(len(config.users)):
#             plist_act.append(plist_sec[x+1][z*userTrackLim:z*userTrackLim+userTrackLim]) # Appends part of user plist based day
#             print()
            
#         random.shuffle(plist_act)
#         plist_mas.append([plist_act])

#         plist_act =[]
#         z += 1



# def create(usersOn):
#     global plist_sec
#     global plist_act
#     global plist_mas
#     global sp

#     plistN = ''

#     plist_sec = plist_org
#     plist_act.append(plist_sec[0][:userTrackLim]) # Appends global playlist
#     for x in range(len(usersOn)):
#         if usersOn[x] == True:
#             plist_act.append(plist_sec[x+1][:userTrackLim]) # Appends part of user plist based day
#     random.shuffle(plist_act)
#     plist_mas.append([plist_act])

#     sp.user_playlist_create(config.spCred[0], "Work-Auto", description="Auto gen work playlist")
#     playlists = sp.user_playlists(config.spCred[0])
#     for playlist in playlists['items']:
#         print(playlist['name'])
#         if playlist['name'] == "Work-Auto":
#             plistN = playlist['name']
    
#     length = len(plist_act)
#     seps = length / 100 + 1

#     z = 0
#     while z < seps:
#         sp.playlist_add_items(config.spCred[0], )
#         # plist_act.append(plist_sec[0][z*userTrackLim:z*userTrackLim+userTrackLim]) # Appends global playlist
#         # for x in range(len(config.users)):
#         #     plist_act.append(plist_sec[x+1][z*userTrackLim:z*userTrackLim+userTrackLim]) # Appends part of user plist based day
#         #     print()
