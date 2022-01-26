import db


def addUser(user, plist):
    conn = db.create_connection(db.database)
    with conn:
        cur = conn.cursor()
        cur.execute('INSERT INTO users (user, plist, downloaded) VALUES (?, ?, 1)', (user, plist))

def deleteUser(user):
    conn = db.create_connection(db.database)
    with conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM users WHERE user = ?", (user,))
        cur.execute("DELETE FROM songs WHERE owner = ?", (user,))

def updateSpot(user, secert):
    conn = db.create_connection(db.database)
    with conn:
        cur = conn.cursor()
        cur.execute("UPDATE spData SET user = ?, pass = ? WHERE id = 1", (user, secert))


def returnUsers():
    conn = db.create_connection(db.database)
    with conn:
        cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    return rows