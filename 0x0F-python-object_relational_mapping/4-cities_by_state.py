#!/usr/bin/python3

"""
    A script that lists all states with a name starting with
    N from the database
"""

import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(
               host="localhost",
               user=sys.argv[1],
               password=sys.argv[2],
               database=sys.argv[3],
               port=3306
            )
    cursor = conn.cursor()
    sql = """SELECT cities.id, cities.name, states.name
    FROM cities JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC"""
    cursor.execute(sql)
    states = cursor.fetchall()
    for state in states:
        print(state)
