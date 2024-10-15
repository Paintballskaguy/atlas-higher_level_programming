#!/usr/bin/python3

"""
This script lists all the states with a name starting with 'N'
only from database hbtn_0e_0_usa

"""

import MySQLdb
from sys import argv


def list_states_starting_with_n():
    print("Connecting to database...")
    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         port=3306)
    print("Connected!")
    
    cur = db.cursor()
    print("Executing query...")
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%; ORDER by id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()

    if __name__ == "__main__":
        list_states_starting_with_n()

