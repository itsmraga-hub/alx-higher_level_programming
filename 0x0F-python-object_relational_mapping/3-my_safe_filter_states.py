#!/usr/bin/python3
import MySQLdb
import sys

db = MySQLdb.connect(host="localhost", user=sys.argv[1], password=sys.argv[2], database=sys.argv[3], port=3306)
cursor = db.cursor()
sql = """SELECT id, name FROM states WHERE name LIKE %s ORDER BY id ASC"""
cursor.execute(sql, (sys.argv[4], ))
states = cursor.fetchall()
for state in states:
    print(state)
