-- a script that displays the top 3 of cities temperature
SELECT city, AVG(value) as avg_temp
FROM temperatures
WHERE MONTH(month) IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;