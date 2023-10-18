-- script that lists all the cities of California in the database hbtn_0d_usa.
SELECT cities.id, cities.name
FROM cities
WHERE state_id = (
	SELECT id
	FROM states
	WHERE name = 'California'
)
