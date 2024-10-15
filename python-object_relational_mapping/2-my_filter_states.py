#!/usr/bin/python3

"""
Script takes in an arugment and displays all state values.    
"""


import MySQLdb
from sys import argv

def find_state_by_name():
    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(argv[4]) cur.execute(query))
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    find_state_by_name()
