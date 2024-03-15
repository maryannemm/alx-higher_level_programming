#!/usr/bin/python3
"""
Script that lists all cities of a given state from the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys

def filter_cities(username: str, password: str, db_name: str, state_name: str):
    """
    Retrieve and print all cities of the given state from the specified database.

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
    cursor.execute("SELECT cities.name FROM cities JOIN states ON cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id ASC", (state_name,))

    # Fetch all the rows and print them
    cities = [row[0] for row in cursor.fetchall()]
    if cities:
        print(", ".join(cities))
    else:
        print("")

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

    filter_cities(username, password, db_name, state_name)

