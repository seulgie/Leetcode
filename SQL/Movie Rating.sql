(
    SELECT name AS results
    FROM MovieRating
    JOIN Users USING(user_id)
    GROUP BY user_id
    ORDER BY COUNT(*) DESC, name
    LIMIT 1
)

UNION ALL

(
    SELECT title AS results
    FROM MovieRating
    JOIN Movies USING(movie_id)
    WHERE created_at BETWEEN '2020-02-01' AND '2020-02-29'
    GROUP BY title
    ORDER BY AVG(rating) DESC, title
    LIMIT 1
)
