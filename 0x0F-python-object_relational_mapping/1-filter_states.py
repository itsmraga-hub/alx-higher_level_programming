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
    sql = """SELECT * FROM `states`"""
    cursor.execute(sql)
    states = cursor.fetchall()
    for state in states:
        if state[1][0] == "N":
            print(state)
