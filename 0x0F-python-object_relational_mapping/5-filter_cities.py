#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa"""

import sys
import MySQLdb
"""modules import"""


if __name__ == '__main__':
    """arguments order"""
    user = sys.argv[1]
    pswrd = sys.argv[2]
    database = sys.argv[3]
    search = sys.argv[4]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=user,
        passwd=pswrd,
        db=database
    )

    cursor = db.cursor()
    cursor.execute("SELECT cities.name FROM cities " +
                   "JOIN states ON cities.state_id = states.id " +
                   "WHERE states.name = %s ORDER BY cities.id;", (search, ))
    result = cursor.fetchall()
    sep = ""
    for row in result:
        print("{}{}".format(sep, row[0]), end="")
        sep = ", "
    print()
    cursor.close()
    db.close()
