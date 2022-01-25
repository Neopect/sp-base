# The purpose of this file is to update the database with the yaml file

# import configRW
import db

database = '/home/tylerm/git/sp-base/test2'


def addUser(user, plist):
    global database
    conn = db.create_connection(database)
    with conn:
        cur = conn.cursor()
        cur.execute('INSERT INTO users (user, plist, downloaded) VALUES (?, ?, 1)', (user, plist))

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


def returnUsers():
    global database
    conn = db.create_connection(database)

    with conn:
        cur = conn.cursor()
    cur.execute("SELECT * FROM users")

    rows = cur.fetchall()

    # for row in rows:
    #     print(row)
    return rows