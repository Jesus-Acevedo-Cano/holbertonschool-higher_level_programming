-- script that lists all cities contained in the database hbtn_0d_usa
USE hbtn_0d_usa;
SELECT cities.id, cities.name, states.name FROM states, cities
ORDER BY cities.id ASC;
