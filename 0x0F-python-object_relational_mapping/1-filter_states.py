#!/usr/bin/python3
import MySQLdb
import sys

"""
    A script that lists all states with a name starting with N
    from the database
"""

if __name__ == "__main__":
    conn = MySQLdb.connect(
               host="localhost",
               user=sys.argv[1],
               password=sys.argv[2],
               database=sys.argv[3],
               port=3306
            )
    cursor = conn.cursor()
    sql = """SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"""
    cursor.execute(sql)
    states = cursor.fetchall()
    for state in states:
        print(state)

    conn.close()
