#!/usr/bin/python3
""" script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument."""
import MySQLdb
import sys

if __name__ == "__main__":
    args = sys.argv
    mysql_username = args[1]
    mysql_password = args[2]
    database_name = args[3]
    state_name = args[4]

    connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name,
            charset="utf8",
    )
    cursor = connection.cursor()

    sql = "SELECT *\
            FROM states\
            WHERE states.name LIKE BINARY '{}%'\
            ORDER BY id ASC".format(state_name)
    cursor.execute(sql)
    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    connection.close()
