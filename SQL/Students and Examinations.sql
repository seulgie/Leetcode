# Write your MySQL query statement below
WITH CTE AS
(
    SELECT *
    FROM Students
    CROSS JOIN Subjects
    ORDER BY student_id, subject_name
),

CTE2 AS
(
    SELECT 
        student_id, 
        subject_name, COUNT(subject_name) AS attended_exams
    FROM Examinations
    GROUP BY student_id, subject_name
    ORDER BY student_id, subject_name
)

SELECT 
    c1.student_id, 
    c1.student_name, 
    c1.subject_name,
    IFNULL(attended_exams, 0) AS attended_exams
FROM CTE AS c1
LEFT JOIN CTE2 AS c2
ON c1.student_id = c2.student_id AND c1.subject_name = c2.subject_name
ORDER BY student_id, subject_name
