#!/usr/bin/python3
""" lists all states from the database """

import sys
import MySQLdb
"""modules import"""


if __name__ == '__main__':
    """arguments order"""
    user = sys.argv[1]
    pswrd = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=user,
        passwd=pswrd,
        db=database
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'" +
                   "ORDER BY states.id ASC")
    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.close()
    db.close()
