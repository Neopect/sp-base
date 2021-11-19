# (AKA config)

import os

confFile = []
spCred = []
gPlayl = []
playl = []
users = []

def genConfig(root, rootConfig):
    # Creates the basic config file for saving
    # and reading data for the program.
    print("Generating config folder...")
    os.mkdir(rootConfig)
    os.chdir(rootConfig)
    os.mkdir('plists')

    print("Generating config file...")
    fw = open("sp", "w")
    # fw.write("Userid\nsecert")
    fw.close()
    fw = open("users", "w")
    fw.close()
    fw = open("globs", "w")
    fw.write("3PGHzE2Tqab3V5xH6JyVcW")
    fw.close()
    

def readConfig(root, rootConfig):
    # Reads config file and sets them
    # in the interrupter's memory
    global id, secret, confFile,  gPlayl
    os.chdir(rootConfig)

    # Reads cred file
    fw = open("sp", "r")
    for x in fw:
        spCred.append(x)
    print(spCred)

    # Reads globs
    fw = open("globs", "r")
    for x in fw:
        print("Adding to global playlist... " + x)
        gPlayl.append(x)
    print(gPlayl)

    # Reads playlists
    fw = open("users", "r")
    for x, val in enumerate(fw):
        if "\n" in val:
            val = val.replace("\n","")
        
        if (x % 2) == 0:
            playl.append(val)
        else:
            print("Adding to playlist... " + val)
            users.append(val)

    print(playl)
    print(users)


            
def configRunner(root, rootConfig):
    # Checks for config folder
    os.chdir(root)

    if (os.path.isdir(rootConfig) == False):
        genConfig(root, rootConfig)
        # quit()
    else:
        readConfig(root, rootConfig)

