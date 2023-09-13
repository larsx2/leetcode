-- Problem: https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/
-- Solution: https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/submissions/1041748778/

WITH Friends(id) AS (
    SELECT requester_id FROM RequestAccepted
    UNION ALL
    SELECT accepter_id FROM RequestAccepted
)
SELECT id, count(*) AS num
FROM Friends
GROUP BY 1
ORDER BY 2 DESC
LIMIT 1
