#!/usr/bin/python3
"""Fetch and display all cities of a given state from the MySQL database hbtn_0e_4_usa."""

import sys
import MySQLdb

if __name__ == "__main__":
    # Check for correct number of arguments
    if len(sys.argv) != 5:
        print("Usage: {} username password database state_name".format(
            sys.argv[0]))
        sys.exit(1)

    # Retrieve arguments
    username, password, database, state_name = sys.argv[1:5]

    # Connect to MySQL server
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
        cursor = db.cursor()

        # Execute SQL query to retrieve cities with their respective states
        query = (
            "SELECT cities.id, cities.name, states.name "
            "FROM cities "
            "JOIN states ON cities.state_id = states.id "
            "ORDER BY cities.id ASC"
        )

        cursor.execute(query)

        # Fetch the result
        result = cursor.fetchone()[0]

        # Display results
        if result:
            print(result)
        else:
            print("No cities found for the state:", state_name)

        # Close cursor and connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error:", e)
        sys.exit(1)
