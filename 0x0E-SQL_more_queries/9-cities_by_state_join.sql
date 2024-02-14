-- Script to list all cities and their corresponding states in the database hbtn_0d_usa
SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE cities.state_id = states.id
ORDER BY cities.id;