--displays the max temperature of each state (ordered by State name)
-- execute cat 103-max_state.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
SELECT state, MAX(temperature) AS max_temp FROM temperatures GROUP BY state ORDER state;
