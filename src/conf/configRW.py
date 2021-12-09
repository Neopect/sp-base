# (AKA config)

import os
import shutil
import yaml

# confFile = []
spCred = []
gPlayl = []
playl = []
users = []

def genConfig(root, rootConfig):
    # Creates the basic config file for saving
    # and reading data for the program.
    print("Generating config folder...")
    path = os.path.join(root, "../../conf/")

    os.mkdir(rootConfig)
    os.chdir(path)

    print("Generating config file...")
    shutil.copy('sample_config.yml', rootConfig+'/config.yml')

    os.chdir(rootConfig)
    os.mkdir('plists')

def readConfig(rootConfig):
    # Reads config file and sets them
    # in the interrupter's memory
    global spCred, users,  gPlayl, playl
    os.chdir(rootConfig)

    with open("config.yml", "r") as ymlconf:
        conf = yaml.safe_load(ymlconf)

    for key, value in conf.items():
        print (key + " : " + str(value))

    # Loads cred info
    spCred.append(conf["Spotify"]["user"])
    spCred.append(conf["Spotify"]["pass"])

    # Loads Globals
    for x in conf["Playlists"]["Globals"]:
        print("Adding to global playlists... " + x)
        gPlayl.append(x)

    # Loads User Playlists
    for x in conf["Playlists"]["Users"]:
        ent = conf["Playlists"]["Users"][x]
        print(ent)
        users.append(ent["name"])
        for y in ent["playlists"]:
            print("Adding to playlists... " + y)
            playl.append([y, ent["name"]])

     
def configRunner(root, rootConfig):
    # Checks for config folder
    os.chdir(root)

    if (os.path.isdir(rootConfig) == False):
        genConfig(root, rootConfig)
        # quit()
    else:
        readConfig(rootConfig)

def hello():
    print("hello world")