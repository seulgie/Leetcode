# Write your MySQL query statement below

SELECT id, SUM(num) AS num
FROM
(
    SELECT requester_id AS id, COUNT(*) AS num
    FROM RequestAccepted
    GROUP BY requester_id

    UNION ALL

    SELECT accepter_id AS id, COUNT(*) AS num
    FROM RequestAccepted
    GROUP BY accepter_id
) AS t
GROUP BY id
ORDER BY SUM(num) DESC
LIMIT 1
