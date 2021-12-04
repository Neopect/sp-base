# (AKA config)

import os
import shutil
import yaml

# confFile = []
spCred = []
gPlayl = []
playl = []
users = []

# def genConfig(root, rootConfig):
#     # Creates the basic config file for saving
#     # and reading data for the program.
#     print("Generating config folder...")
#     os.mkdir(rootConfig)
#     os.chdir(rootConfig)
#     os.mkdir('plists')

#     print("Generating config file...")
#     fw = open("sp", "w")
#     # fw.write("Userid\nsecert")
#     fw.close()
#     fw = open("users", "w")
#     fw.close()
#     fw = open("globs", "w")
#     fw.write("3PGHzE2Tqab3V5xH6JyVcW")
#     fw.close()

def genConfig(root, rootConfig):
    # Creates the basic config file for saving
    # and reading data for the program.
    print("Generating config folder...")
    path = os.path.join(root, "conf/")

    os.mkdir(rootConfig)
    os.chdir(path)

    print("Generating config file...")
    shutil.copy('sample_config.yml', rootConfig+'/config.yml')

    os.chdir(rootConfig)
    os.mkdir('plists')


# def readConfig(root, rootConfig):
#     # Reads config file and sets them
#     # in the interrupter's memory
#     global id, secret, confFile,  gPlayl
#     os.chdir(rootConfig)

#     # Reads cred file
#     fw = open("sp", "r")
#     for x in fw:
#         spCred.append(x)
#     print(spCred)

#     # Reads globs
#     fw = open("globs", "r")
#     for x in fw:
#         print("Adding to global playlist... " + x)
#         gPlayl.append(x)
#     print(gPlayl)

#     # Reads playlists
#     fw = open("users", "r")
#     for x, val in enumerate(fw):
#         if "\n" in val:
#             val = val.replace("\n","")
        
#         if (x % 2) == 0:
#             playl.append(val)
#         else:
#             print("Adding to playlist... " + val)
#             users.append(val)

#     print(playl)
#     print(users)

def readConfig(rootConfig):
    # Reads config file and sets them
    # in the interrupter's memory
    global spCred, users,  gPlayl, playl
    os.chdir(rootConfig)

    with open("config.yml", "r") as ymlconf:
        conf = yaml.load(ymlconf)

    # Loads cred info
    spCred.append[conf["Spotify"["user"]]]
    spCred.append[conf["Spotify"["pass"]]]

    # Loads Globals
    for x in conf["Playlists"["Globals"]]:
        print("Adding to global playlists... " + x)
        gPlayl.append(x)

    # Loads User Playlists
    for x in conf["Playlists"["Users"]]:
        users.append(x["name"])
        for y in x["playlists"]:
            print("Adding to playlists... " + y)
            playl.append([y, x["name"]])


    print(playl)
    print(users)

            
def configRunner(root, rootConfig):
    # Checks for config folder
    os.chdir(root)

    if (os.path.isdir(rootConfig) == False):
        genConfig(root, rootConfig)
        # quit()
    else:
        readConfig(rootConfig)

