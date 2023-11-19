#!/usr/bin/python3
"""Fetch and display states based on the provided state name."""

import sys
import MySQLdb

if __name__ == "__main__":
    # Check for correct number of arguments
    if len(sys.argv) != 5:
        script_name = sys.argv[0]
        print(f"Usage: {script_name} username password database state_name")
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

        # Execute SQL query safely with parameterized query
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        cursor.execute(query, (state_name,))

        # Fetch all results
        results = cursor.fetchall()

        # Display results
        for row in results:
            print(row)

        # Close cursor and connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error:", e)
        sys.exit(1)
