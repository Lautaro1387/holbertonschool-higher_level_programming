#!/usr/bin/python3
"""
    takes in an argument and displays all values in the states table
"""
from MySQLdb import connect
import sys


if __name__ == "__main__":
    _user = sys.argv[1]
    _pass = sys.argv[2]
    _db = sys.argv[3]
    _st = sys.argv[4]

    db = connect(host="localhost", port=3306, user=_user,
                 password=_pass, db=_db)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE states.name = %s\
            ORDER BY states.id ASC", [_st])
    rows = cur.fetchall()
    for row in rows:
        if row[1] == _st:
            print(row)
    cur.close()
    db.close()
