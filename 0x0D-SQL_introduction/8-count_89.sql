-- select where id is 89
--execute cat 8-count_89.sql | mysql -hlocalhost -uroot -p hbtn_0c_0 | tail -1
SELECT COUNT(*) FROM first_table WHERE id = 89;
