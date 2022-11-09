#!/usr/bin/python3
"""Lists all states from the databases hbtn_0e_0_usa"""

from MySQLdb import connect
import sys


if __name__ == "__main__":
    _user = sys.argv[1]
    _pass = sys.argv[2]
    _db = sys.argv[3]

    db = connect(host="localhost", port=3306, user=_user, passwd=_pass, db=_db)
    curs = db.cursor()
    curs.execute("SELECT * FROM states ORDER BY states.id")
    rows = curs.fetchall()
    for row in rows:
        print(row)
    curs.close()
    db.close()