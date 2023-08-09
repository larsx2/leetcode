-- Problem: https://leetcode.com/problems/consecutive-numbers/
-- Solution: https://leetcode.com/problems/consecutive-numbers/submissions/1016163272/

SELECT DISTINCT q.num AS ConsecutiveNums
FROM (
  SELECT
    num,
    id,
    LAG(id, 1) OVER(ORDER BY id) AS prev_id,
    LAG(id, 2) OVER(ORDER BY id) AS first_id,
    LAG(num, 1) OVER(ORDER BY id) AS prev_num,
    LAG(num, 2) OVER(ORDER BY id) AS first_num
  FROM Logs) AS q
WHERE
  q.num = q.prev_num AND
  q.prev_num = q.first_num AND
  q.id = (q.prev_id + 1) AND
  q.prev_id = (q.first_id + 1)
