-- Problem: https://leetcode.com/problems/game-play-analysis-iv/
-- Solution: https://leetcode.com/problems/game-play-analysis-iv/submissions/1028036515/

WITH FIRST_LOGGED_DATE AS (
  SELECT player_id, MIN(event_date) AS first_login_date
  FROM Activity
  GROUP BY player_id
)
SELECT
    ROUND(COUNT(*) / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS fraction
FROM Activity a JOIN FIRST_LOGGED_DATE b
  ON a.player_id = b.player_id AND DATEDIFF(a.event_date, b.first_login_date) = 1
