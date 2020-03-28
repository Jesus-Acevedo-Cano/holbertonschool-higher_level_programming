#!/usr/bin/python3
"""script that takes an argument and displays all values in the states table"""

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
    cursor.execute("SELECT * FROM states WHERE name = '" + search + "'" +
                   "ORDER BY states.id ASC".format(search))
    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.close()
    db.close()
