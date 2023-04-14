#!/usr/bin/python3
import MySQLdb
import sys

"""
    A script that takes in an argument and displays all
    values in the states table of hbtn_0e_0_usa
    where name matches the argument.
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
    sql = """SELECT id, name FROM states WHERE name = '{}'"""
    cursor.execute(sql.format(sys.argv[4]))
    states = cursor.fetchall()
    for state in states:
        print(state)
    conn.close()
