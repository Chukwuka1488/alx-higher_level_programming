#!/usr/bin/python3
"""Fetch and display states starting with 'N' from the MySQL database."""

import sys
import MySQLdb

if __name__ == "__main__":
    # Check for correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    # Retrieve arguments
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to MySQL server
    try:
        db = MySQLdb.connect(host="localhost", port=3306,
                             user=username, passwd=password, db=database)
        cursor = db.cursor()

        # Execute SQL query to retrieve states starting with 'N'
        query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
        cursor.execute(query)

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
