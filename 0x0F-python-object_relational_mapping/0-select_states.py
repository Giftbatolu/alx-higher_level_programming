#!/usr/bin/python3

import MySQLdb
from sys import argv

my_db = MySQLdb.connect(
    host="localhost",
    user=argv[1],
    passwd=argv[2],
    port=3306,
    db=argv[3]
)
cur_sor = my_db.cursor()
cur_sor.excute("SELECT * FROM states ORDER BY id ASC")

result_rows = cur_sor.fetchall()

for row in result_rows:
    print(row)

if __name__ == "__main__":
    import sys
