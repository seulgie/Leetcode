# Write your MySQL query statement below
WITH CTE1 AS
(
    SELECT
        u.product_id,
        purchase_date,
        units,
        price,
        units * price AS total_price
    FROM UnitsSold AS u
    CROSS JOIN Prices AS p
    WHERE purchase_date BETWEEN start_date AND end_date
    AND p.product_id = u.product_id
    ORDER BY product_id
),

CTE2 AS
(
    SELECT
        p.product_id,
        0 AS average_price
    FROM Prices AS p
    LEFT JOIN UnitsSold AS u
    ON p.product_id = u.product_id
    WHERE u.product_id IS NULL
)

SELECT product_id, ROUND(SUM(total_price) / SUM(units), 2) AS average_price
FROM CTE1
GROUP BY product_id

UNION ALL

SELECT *
FROM CTE2
