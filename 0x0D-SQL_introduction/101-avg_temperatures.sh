#!/bin/bash

# Import the temperatures.sql file into the hbtn_0c_0 database
mysql -h localhost -u root -p hbtn_0c_0 < temperatures.sql

# Execute the SQL query to calculate the average temperature by city
mysql -h localhost -u root -p hbtn_0c_0 << EOF
SELECT city, AVG(temperature) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
EOF

