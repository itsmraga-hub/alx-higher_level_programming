#!/usr/bin/python3

"""
    A script that lists all states with a name starting with N
    from the database
"""

import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(
               user=sys.argv[1],
               password=sys.argv[2],
               database=sys.argv[3],
            )
    cursor = conn.cursor()
    sql = """SELECT * FROM `states` WHERE name LIKE 'N%' ORDER BY id ASC"""
    cursor.execute(sql)
    states = cursor.fetchall()
    for state in states:
        print(state)
