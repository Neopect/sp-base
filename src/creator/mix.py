import random
import math
import dbCreator as db

# def exceptions():
#     pass

def dupCheck(plist):
    pass

def explicit_check(plists):
    # Explicit check
    for plist in range(len(plists)):
            for song in range(len(plist)):
                if song[4] == "True":
                    del plists[plist][song]
    return plist

def randPlist(users, prePlist, tracklim = 50, explicit = True):
    # Creates random playlist from set of users
    plists = []
    plist_final = []

    # Either copy or append playlists from user
    if prePlist != None or prePlist != []:
        plists = prePlist
    else:
        for x in users:
            plists.append(db.fetchPlist(x))


    #TODO Dup check

    # Explicit check
    if explicit == True:
        plists = explicit_check(plists)


    # Take $tracklim out of each list at a time
    for x in range(len(plists)):
        random.shuffle(plists[x])
        try:
            plist_final.append(plists[x][:tracklim])
        except:
            plist_final.append(plists[x])

    # Randomize and return
    random.shuffle(plist_final)
    return plist_final



def dayMix(users, prePlist, tracklim = 50, explicit = True, days = 2):
    
    plists, plist_sep, plists_mixed = []

    # Either copy or append playlists from user
    if prePlist != None or prePlist != []:
        plists = prePlist
    else:
        for x in users:
            plists.append(db.fetchPlist(x))


    #TODO Dup check

    # Explicit check
    if explicit == True:
        plists = explicit_check(plists)


    # Splits the each playlist evenly between # of days into a group
    for plist in plists:
        random.shuffle(plist)
        length = len(plist)
        lengthD = math.floor(length/days)

        plist_tmp = []
        i = 0
        while i < days-1:
            plist_tmp.append(plist[i*lengthD:i*lengthD+lengthD])
            i += 1
        plist_sep.append(plist_tmp)

    # Combines each playlist into one
    i = 1
    while i < days:
        plist_tmp = []
        for plist in range(len(plists)):
            try:
                plist_tmp.append(plist_sep[plist][i-1][:tracklim])
            except:
                plist_tmp.append(plist_sep[plist][i-1])
        
        plists_mixed.append(plist_tmp)
        i += 1

    return plists_mixed

