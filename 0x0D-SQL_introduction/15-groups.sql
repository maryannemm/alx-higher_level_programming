-- lists the number of records with the same score in the table second_table
-- execute cat 15-groups.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
