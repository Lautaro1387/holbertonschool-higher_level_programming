#!/usr/bin/python3
"""
lists all states with a name starting with N from the database hbtn_0e_0_usa
"""


from MySQLdb import connect
import sys

if __name__ == "__main__":
    _user = sys.argv[1]
    _pass = sys.argv[2]
    _db = sys.argv[3]

    db = connect(host="localhost", port=3006, user=_user, passwd=_pass, db=_db)
    curs = db.cursor()
    curs.execute("SELECT * FROM states ORDER BY states.id asc")
    rows = curs.fetchall()
    for row in rows:
        if row[1][0] == 'N':
            print(row)
