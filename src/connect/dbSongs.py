# The purpose of this file is to update the database with the yaml file

# import configRW
import sys
sys.path.insert(0, 'src/conf')
import db as db

database = '/home/tylerm/git/sp-base/test2'


def addSong():
    pass

def deleteSong():
    pass

def addPlist(plist, owner):
    global database

    # plist_conv = '('
    plist_conv = '('
    first = True
    for song in plist: # Creates a long string of all the songs to add
        if first != True:
            plist_conv += ', ('
        
        items = '"'
        for item in song:

            if '"' in str(item):
                item = str(item).replace('"',"")

            items += str(item) + '", "'
        plist_conv += items + song[4] +  '", "' + owner + '")' # TODO Make the plist reflect the actual plist uri
        first = False
    plist_conv += ';'
    print(plist_conv)

    conn = db.create_connection(database)
    with conn:
        cur = conn.cursor()
        prefix = "INSERT INTO songs (song, artist, time, explicit, spotid, previewurl, genre, mood, plist, owner) VALUES "
        command = prefix + plist_conv # This is a really stupid way to solve the issue but it works, so ha
        cur.execute(command)
    

def deletePlist(plist='NULL', owner='NULL'):
    global database
    conn = db.create_connection(database)
    with conn:
        cur = conn.cursor()
        if plist != 'NULL':
            cur.execute("DELETE FROM songs WHERE plist = ?", (plist,))
        else:
            cur.execute("DELETE FROM songs WHERE owner = ?", (owner,))

def listSongs():
    global database
    conn = db.create_connection(database)

    with conn:
        cur = conn.cursor()
    cur.execute("SELECT * FROM songs")

    rows = cur.fetchall()

    # for row in rows:
    #     print(row)
    return rows

def listPlist(plist):
    global database
    conn = db.create_connection(database)

    with conn:
        cur = conn.cursor()
    cur.execute("SELECT * FROM songs WHERE plist = ?", (plist,))

    rows = cur.fetchall()

    # for row in rows:
    #     print(row)
    return rows