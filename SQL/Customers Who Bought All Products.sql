SELECT customer_id
FROM   customer
GROUP  BY customer_id
HAVING Group_concat(DISTINCT(product_key) ORDER BY product_key) = (SELECT
       Group_concat(DISTINCT(product_key) ORDER BY product_key)
                                                                   FROM
       product) 
