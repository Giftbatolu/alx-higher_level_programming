#!/usr/bin/python3

""" A script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa """

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """ Execute the code if not imported """

    my_db = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        passwd=argv[2],
        port=3306,
        db=argv[3]
        )
    cur_sor = my_db.cursor()
    cur_sor.execute(
        "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    result_rows = cur_sor.fetchall()

    for row in result_rows:
        print(row)
