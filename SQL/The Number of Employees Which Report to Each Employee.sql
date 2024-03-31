# Write your MySQL query statement below
SELECT
    e1.reports_to AS employee_id,
    e2.name AS name,
    COUNT(e1.employee_id) AS reports_count,
    ROUND(AVG(e1.age), 0) AS average_age
FROM Employees e1, Employees e2
WHERE e1.reports_to = e2.employee_id
AND e1.reports_to IS NOT NULL
GROUP BY 
    e1.reports_to, 
    e2.name
ORDER BY e2.employee_id
