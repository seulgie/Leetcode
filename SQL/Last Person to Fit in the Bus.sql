SELECT person_name
FROM 
(
    SELECT 
        person_id,
        person_name,
        weight,
        SUM(weight) OVER(ORDER BY turn ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS total_weight
    FROM Queue
    ORDER BY turn
) AS t
WHERE t.total_weight <= 1000
ORDER BY total_weight DESC
LIMIT 1
