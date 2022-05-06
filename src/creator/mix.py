import random
import math


def dupCheck(plist):
    # TODO Finish code
    return plist


def explicit_check(plists, single=False):
    # Explicit check

    if (single == False):
        for song in range(len(plists)):
                if song[4] == "True":
                    del plists[song]
        return plists

    for plist in range(len(plists)):
            for song in range(len(plist)):
                if song[4] == "True":
                    del plists[plist][song]
    return plists


def randPlist(plists, tracklim = 50, explicit = True):
    # Creates random playlist from set of users
    # TODO Add playlist max limit
    # TODO Add bias
    plist = []

    # Dup check
    plists = dupCheck(plists)

    # Explicit check
    if explicit == True:
        plists = explicit_check(plists)


    # Take $tracklim out of each list at a time
    for x in range(len(plists)):
        random.shuffle(plists[x])
        try:
            plist.append(plists[x][:tracklim])
        except:
            plist.append(plists[x])

    # Randomize and return
    random.shuffle(plist)
    return plist



def dailyMix(plists, tracklim = 50, explicit = True, days = 2):
    
    plist_sep, plists_mixed = []

    # Dup check
    plists = dupCheck(plists)

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
                plist_tmp.append(plist_sep[plist][i-1][:tracklim]) # Test if appends properly
            except:
                plist_tmp.append(plist_sep[plist][i-1])
        
        plists_mixed.append(plist_tmp)
        i += 1

    return plists_mixed

