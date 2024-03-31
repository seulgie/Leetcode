# Write your MySQL query statement below
SELECT *
FROM Users
WHERE mail REGEXP '^[A-Za-z][0-9a-zA-Z\.\_\-]*@leetcode\\.com$'
