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
    sql = """SELECT cities.name FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s ORDER BY cities.id ASC"""
    cursor.execute(sql, (sys.argv[4], ))
    states = cursor.fetchall()
    for i, state in enumerate(states):
        if i < len(states) - 1:
            print(state[0], end=", ")
        else:
            print(state[0], end="")
    print()
    cursor.close()

    conn.close()
