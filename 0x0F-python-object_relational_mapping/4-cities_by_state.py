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

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=user,
        passwd=pswrd,
        db=database
    )

    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name " +
                   "FROM cities LEFT JOIN states " +
                   "ON cities.state_id = states.id " +
                   "ORDER BY cities.id ASC")
    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.close()
    db.close()
