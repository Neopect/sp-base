import sqlite3
from sqlite3 import Error

global database 
database = '/home/tylerm/git/sp-base/test2'

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def customCommand(message):
    global database
    conn = create_connection(database)
    with conn:
        cur = conn.cursor()
        cur.execute(message)
    rows = cur.fetchall()

    for row in rows:
        print(row)
    return rows

# == SAMPLE FUNCTION ==
# def select_task_by_priority(conn, priority):
#     """
#     Query tasks by priority
#     :param conn: the Connection object
#     :param priority:
#     :return:
#     """
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM tasks WHERE priority=?", (priority,))

#     rows = cur.fetchall()

#     for row in rows:
#         print(row)
