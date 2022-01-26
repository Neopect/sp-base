import random
import math
import dbCreator as db

def exceptions():
    pass

def dupCheck(plist):
    pass

def randPlist(users, tracklim = 50, explicit = True):
    # Creates random playlist from set of users
    plists = []
    plist_final = []

    # Append playlists from user
    for x in users:
        plists.append(db.fetchPlist(x))

    #TODO Dup check

    # Explicit check
    if(explicit == False):
        for plist in range(len(plists)):
            for song in range(len(plist)):
                if song[4] == "True":
                    del plists[plists][song]



    # Take $tracklim out of each list at a time
    for x in range(len(plists)):
        random.shuffle(plists[x])
        try:
            plist_final.append(plists[x[:tracklim]])
        except:
            plist_final.append(plists[x])

    # Randomize and return
    random.shuffle(plist_final)
    return plist_final



def dayMix(users, tracklim = 50, days = 1, explicit = True):
    pass

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

