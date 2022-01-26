import random
import math
import dbCreator as db

def exceptions():
    pass


def randPlist(users, tracklim = 50, explicit = False):
    # Creates random playlist from set of users
    plists = []
    plist_final = []

    # Append playlists from user
    for x in users:
        plists.append(db.fetchPlist(x))

    # Randomize each plist
    for x in range(len(plists)):
        random.shuffle(plists[x])

    # Take $tracklim out of each list at a time
    for x in range(len(plists)):
        try:
            plist_final.append(plists[x[:tracklim]])
        except:
            plist_final.append(plists[x])

    # Randomize and return
    random.shuffle(plist_final)
    return plist_final



def randPlist(plists, tracklim = 50, globs = list(), globlim = 50):
    # Creates random playlist from set of users

    plist_final = []

    # Randomize each plist
    for x in range(len(plists)):
        random.shuffle(plists[x])
        
    for x in range(len(globs)):
        random.shuffle(globs[x])

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

def dailyMix(plists, tracklim = 50, globs = list(), globlim = 50, days = 1, exceptions = False):
    # Creates a daily mix playlist for a set number of days
    plists_SP = []
    plists_mixed = []

    # Splits the playlists into sets of days
    for plist in plists:
        random.shuffle(plist)
        length = len(plist)
        lengthD = math.floor(length/days)

        plist_tmp = []
        i = 0
        while i < days-1:
            plist_tmp.append(plist[i*lengthD:i*lengthD+lengthD])
            i += 1
        plists_SP.append(plists_SP)

    i = 1
    while i < days:
        plist_tmp = []
        for plist in plists:
            plist_tmp.append(plist[i-1])
        plists_mixed.append(randPlist(plist_tmp, tracklim, globs, globlim))
        i += 1

    return plists_mixed

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
