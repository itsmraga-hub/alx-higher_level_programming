#!/usr/bin/python3

"""
    A script that takes in an argument and displays all
    values in the states table of hbtn_0e_0_usa
    where name matches the argument.
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
    sql = """SELECT * FROM `states` WHERE BINARY `name` = '{}'"""
    cursor.execute(sql.format(sys.argv[4]))
    states = cursor.fetchall()
    for state in states:
        print(state)
