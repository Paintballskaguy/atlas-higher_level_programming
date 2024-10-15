#!/usr/bin/python3
"""
Script to list all cities from the database.
"""
import MySQLdb
from sys import argv


def list_cities():
    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         port=3306)

    cur = db.cursor()

    query = ("SELECT cities.id, cities.name, states.name FROM cities "
             "JOIN states ON cities.state_id = states.id "
             "ORDER BY cities.id ASC")
    cur.execute(query)

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    list_cities()
