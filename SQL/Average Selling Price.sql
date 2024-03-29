# Write your MySQL query STATEMENT below
WITH cte1
AS
  (
             SELECT     u.product_id,
                        purchase_date,
                        units,
                        price,
                        units * price AS total_price
             FROM       unitssold     AS u
             CROSS JOIN prices        AS p
             WHERE      purchase_date BETWEEN start_date AND        end_date
             AND        p.product_id = u.product_id
             ORDER BY   product_id ),
  cte2
AS
  (
            SELECT    p.product_id,
                      0         AS average_price
            FROM      prices    AS p
            LEFT JOIN unitssold AS u
            ON        p.product_id = u.product_id
            WHERE     u.product_id IS NULL )
  SELECT   product_id,
           round(sum(total_price) / sum(units), 2) AS average_price
  FROM     cte1
  GROUP BY product_id
  UNION ALL
  SELECT *
  FROM   cte2
