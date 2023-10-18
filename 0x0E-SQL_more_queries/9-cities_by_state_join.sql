-- script that lists all cities contained in the database

-- Lists all cities and show the name of their state
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states
ON cities.id = states.id
ORDER BY cities.id ASC;
