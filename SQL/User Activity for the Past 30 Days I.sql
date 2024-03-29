# Write your MySQL query statement below
SELECT activity_date              AS day,
       Count(DISTINCT( user_id )) AS active_users
FROM   activity
GROUP  BY activity_date
HAVING activity_date BETWEEN Date_add('2019-07-27', INTERVAL -29 day) AND
                             '2019-07-27' 
