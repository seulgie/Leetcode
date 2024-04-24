WITH CTE AS 
(
    SELECT
        num,
        LEAD(num, 1) OVER() num1,
        LEAD(num, 2) OVER() num2
    FROM Logs
)

SELECT DISTINCT(num) AS ConsecutiveNums
FROM CTE
WHERE (num=num1) AND (num=num2)
