#!/usr/bin/python3
"""
Script to display all states where the name matches user-input
safe from SQL injections  
"""
import MySQLdb
from sys import argv


def find_state_by_name_safe():
    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         port=3306)

    cur = db.cursor()

    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (argv[4],))

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    find_state_by_name_safe()