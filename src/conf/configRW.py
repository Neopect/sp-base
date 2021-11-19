# (AKA config)

import os

confFile = []
# id = "null"
# secret = "null"
spCred = []
gPlayl = []
playl = []
users = []
root = None
rootConfig = None

def genConfig():
    # Creates the basic config file for saving
    # and reading data for the program.
    print("Generating config folder...")
    os.mkdir(rootConfig)
    os.chdir(rootConfig)

    print("Generating config file...")
    fw = open("sp", "w")
    # fw.write("Userid\nsecert")
    fw.close()
    fw = open("users", "w")
    fw.close()
    fw = open("globs", "w")
    fw.write("3PGHzE2Tqab3V5xH6JyVcW")
    fw.close()
    

def readConfig():
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


            
def configRunner():
    # Checks for config folder
    global root, rootConfig
    root = os.path.dirname(os.path.abspath(__file__))
    rootConfig = os.path.join(root, "configure")
    os.chdir(root)

    # config_exists = os.path.isdir(path)
    if (os.path.isdir(rootConfig) == False):
        genConfig()
        # quit()
    else:
        readConfig()


def appendData(file, data):
    None