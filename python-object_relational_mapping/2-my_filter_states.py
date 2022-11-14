#!/usr/bin/python3
"""
    takes in an argument and displays all values in
    the states table of hbtn_0e_0_usa where name matches the argument.
"""


from MySQLdb import connect
import sys

if __name__ == "__main__":
    _user = sys.argv[1]
    _pass = sys.argv[2]
    _db = sys.argv[3]
    _st = sys.argv[4]

    db = connect(host="localhost", port=3306, user=_user, passwd=_pass, db=_db)
    curs = db.cursor()
    curs.execute("SELECT * FROM states WHERE states.name='{}'\
            ORDER BY states.id asc".format(_st))
    rows = curs.fetchall()
    for row in rows:
        if row[1] == _st:
            print(row)
    curs.close()
    db.close()
