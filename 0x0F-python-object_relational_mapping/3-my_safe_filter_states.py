#!/usr/bin/python3

"""
    A script that takes in arguments and displays all values
    in the states table of hbtn_0e_0_usa where name matches
    the argument. But this time, write one that is safe
    from MySQL injections!
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
    sql = """SELECT * FROM `states` WHERE name LIKE %s ORDER BY id ASC"""
    cursor.execute(sql, (sys.argv[4], ))
    states = cursor.fetchall()
    for state in states:
        print(state)

    conn.close()
