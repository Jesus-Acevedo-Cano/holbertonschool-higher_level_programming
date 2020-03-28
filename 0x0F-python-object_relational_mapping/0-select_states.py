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
        """conect to data base"""
        host="localhost",
        user=user,
        passwd=pswrd,
        db=database,
        port=3306
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    records = cursor.fetchall()
    for row in records:
        print(row)
    cursor.close()
    db.close()
