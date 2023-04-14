#!/usr/bin/python3
import MySQLdb
import sys

conn = MySQLdb.connect(host="localhost", user=sys.argv[1], password=sys.argv[2], database=sys.argv[3], port=3306)
cursor = conn.cursor()
sql = """SELECT id, name FROM states ORDER BY id ASC""";
cursor.execute(sql)
states = cursor.fetchall()
for state in states:
    print(state)

conn.close()
