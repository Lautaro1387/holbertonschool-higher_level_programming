#!/usr/bin/python3
"""lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa"""


import MySQLdb
import sys

if __name__ = "__main__":
    _user = sys.argv[1]
    _passwd = sys.argv[2]
    _db = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3006, user=_user, passwd=_passwd, db=_db)
    curs = db.cursor()
    curs.execute("SELECT * FROM states ORDER BY states.id asc")
    rows = curs.fetchall()
    for row in rows:
        row[1] == 'N'
        print(row)
