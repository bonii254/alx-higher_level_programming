#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    args = sys.argv
    mysql_username = args[1]
    mysql_password = args[2]
    database_name = args[3]

    connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name,
            charset="utf8",
            )
    cursor = connection.cursor()
    query = "SELECT cities.id, cities.name, states.name\
            FROM states\
            JOIN cities\
            ON states.id = cities.state_id\
            ORDER BY cities.id"
    cursor.execute(query)
    query_result = cursor.fetchall()

    for row in query_result:
        print(row)

    cursor.close()
    connection.close()
