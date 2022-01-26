import sys

sys.path.insert(0, '../conf')
import db as db

database = '/home/tylerm/git/sp-base/test2'


def fetchPlist(owner='', plist=''):
    global database
    conn = db.create_connection(database)
    with conn:
        cur = conn.cursor()
        if owner != '':
            cur.execute("SELECT * FROM songs WHERE owner = ?", (owner,))
        else:
            cur.execute("SELECT * FROM songs WHERE plist = ?", (plist,))

    rows = cur.fetchall()

    # for row in rows:
    #     print(row)
    return rows


# tester = fetchPlist(owner='Tyler')
# a = tester[0][2]
# print(a)
