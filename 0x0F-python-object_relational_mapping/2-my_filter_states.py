#!/usr/bin/python3
"""
Script that displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys

def filter_states(username: str, password: str, db_name: str, state_name: str):
    """
    Retrieve and print all values in the states table where name matches the argument.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        db_name (str): Name of the database.
        state_name (str): Name of the state to search for.

    Returns:
        None
    """
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=db_name)

    # Create a cursor object
    cursor = db.cursor()

    # Execute the query
    cursor.execute("SELECT * FROM states WHERE name=%s ORDER BY id ASC", (state_name,))

    # Fetch all the rows and print them
    for row in cursor.fetchall():
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    filter_states(username, password, db_name, state_name)

