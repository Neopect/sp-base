# The purpose of this file is to update the database with the yaml file

import configRW
import db

database = '/home/tylerm/git/sp-base/test2'


# def updateFromConfig():
#     '''
#     Update users table from config.
#     -1 Needs to pull users from db
#     -2 Compare whats new or old
#     -3 Removes missing users & playlists
#     -4 Adds new users
#     '''
#     global database
#     dbnames, dbadd, dbremove = []
#     conn = db.create_connection(database)
#     with conn:
#         cur = conn.cursor()
#         cur.execute("SELECT user FROM users") # Step 1a
#         rows = cur.fetchall()

#     # Step 1b
#     for row in rows:
#         dbnames.append(row[0])

#     # Step 2a
#     for index, confName in enumerate(configRW.users):
#         if confName not in dbnames:
#             dbadd.append([confName, index])
    
#     # Step 2b
#     for dbName in dbnames:
#         if dbName not in configRW.users:
#             dbremove.append(dbName)

    
#     # Step 3 & 4
#     with conn:
#         cur = conn.cursor()
#         for name in dbremove:
#             cur.execute("DELETE FROM users WHERE user = '?'", (name,))
#             cur.execute("DELETE FROM songs WHERE owner = '?'", (name,))
        
#         for name in dbadd:
#             cur.execute('INSERT INTO users (user, plist, download) VALUES (?, ?, 1)', (name[0], configRW.playl[name[1][0]]))
        


# updateFromConfig()

# def updateAllData():
#     pass

# def updateNewData():
#     pass

def addUser(user, plist):
    global database
    conn = db.create_connection(database)
    with conn:
        cur = conn.cursor()
        cur.execute('INSERT INTO users (user, plist, download) VALUES (?, ?, 1)', (name, plist))

def deleteUser(user):
    global database
    conn = db.create_connection(database)
    with conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM users WHERE user = ?", (user,))
        cur.execute("DELETE FROM songs WHERE owner = ?", (user,))

def updateSpot(user, secert):
    global database
    conn = db.create_connection(database)
    with conn:
        cur = conn.cursor()
        cur.execute("UPDATE spData SET user = ?, pass = ? WHERE id = 1", (user, secert))