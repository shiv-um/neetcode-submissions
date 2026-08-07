-- Write your query below
WITH ordered AS (
    SELECT x,
        LAG(x) OVER(
            ORDER BY x
        ) AS prev_x
    FROM point
)
SELECT MIN(x - prev_x) AS shortest
FROM ordered
WHERE prev_x IS NOT NULL;