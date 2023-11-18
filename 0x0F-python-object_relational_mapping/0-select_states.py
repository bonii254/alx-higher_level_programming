#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""

if __name__ == "__main__":

    import MySQLdb
    import sys

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
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    querry_rows = cursor.fetchall()

    for row in querry_rows:
        print(row)

    cursor.close()
    connection.close()
