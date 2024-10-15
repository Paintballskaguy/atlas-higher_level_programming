#!/usr/bin/python3
"""
Script to take the name of the state and list all the cities in that
state. script is safe from sql injections
"""
import MySQLdb
from sys import argv


def list_cities_by_state():
    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         port=3306)

    cur = db.cursor()

    query = ("SELECT cities.name FROM cities "
             "JOIN states ON cities.state_id = states.id "
             "WHERE states.name = %s "
             "ORDER BY cities.id ASC")
    cur.execute(query, (argv[4],))

    rows = cur.fetchall()

    cities = [row[0] for row in rows]
    print(", ".join(cities))

    cur.close()
    db.close()


if __name__ == "__main__":
    list_cities_by_state()
