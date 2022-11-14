#!/usr/bin/python3
"""
takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa
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
    cur.execute("SELECT cities.name FROM cities LEFT JOIN states ON\
            cities.state_id=states.id WHERE states.name=%s\
            ORDER BY states.id ASC", [_st])
    rows = cur.fetchall()
    for idx, row in enumerate(rows):
        if idx == len(rows) - 1:
            print(f"{row[0]}", end="")
        else:
            print(f"{row[0]}, ", end="")
    print("")
    cur.close()
    db.close()
