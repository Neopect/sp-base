import sys

sys.path.insert(0, '../conf')
import db as db


def fetchPlist(owner='', plist=''):
    conn = db.create_connection(db.database)
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
