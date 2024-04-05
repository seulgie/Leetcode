# Write your MySQL query statement below
WITH c AS 
(
    SELECT
        user_id,
        SUM(IF(action = 'timeout', 1, 0)) as timeout,
        SUM(IF(action = 'confirmed', 1, 0)) as confirmed
    FROM Confirmations
    GROUP BY user_id
)


SELECT
    s.user_id,
    CASE 
        WHEN confirmed = 0 OR c.user_id IS NULL THEN 0
        ELSE ROUND(confirmed / (confirmed + timeout), 2)
        END AS confirmation_rate
FROM Signups s
LEFT JOIN c
ON s.user_id = c.user_id


# Another solution
SELECT
    s.user_id,
    ROUND(AVG(IF(c.action="confirmed", 1, 0)), 2) AS confirmation_rate
FROM Signups s 
LEFT JOIN Confirmations c
ON s.user_id = c.user_id
GROUP BY user_id

