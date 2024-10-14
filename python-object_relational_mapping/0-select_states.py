#!/usr/bin/python3
"""
This script lists all states from hbtn_0e_0_usa.
"""


import MySQLdb
from sys import argv


def list_states():

    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    list_states()
    