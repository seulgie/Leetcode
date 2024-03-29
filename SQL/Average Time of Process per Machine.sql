# Write your MySQL query statement below
SELECT t1.machine_id,
       Round(Avg(t2.timestamp - t1.timestamp), 3) AS processing_time
FROM   activity t1
       LEFT JOIN activity t2
              ON t1.machine_id = t2.machine_id
                 AND t1.process_id = t2.process_id
                 AND t1.activity_type = 'start'
                 AND t2.activity_type = 'end'
GROUP  BY t1.machine_id 
