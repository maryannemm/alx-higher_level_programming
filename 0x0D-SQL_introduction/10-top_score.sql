--ists all records of the table second_table
--execute cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
SELECT score, name FROM second_table ORDER BY score DESC;
