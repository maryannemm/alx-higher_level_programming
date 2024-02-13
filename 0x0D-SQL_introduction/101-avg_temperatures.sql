-- displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
-- execute cat 101-avg_temperatures.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
SELECT city, ROUND(AVG(temperature), 4) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
