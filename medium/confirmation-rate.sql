-- Problem: https://leetcode.com/problems/confirmation-rate/
-- Solution: https://leetcode.com/problems/confirmation-rate/submissions/1012502880/

WITH ConfirmationStats AS (
    SELECT
        user_id,
        ROUND(SUM(
            CASE
                WHEN action='confirmed' THEN 1
                ELSE 0
            END) / COUNT(*), 2) AS confirmation_rate
    FROM Confirmations
    GROUP BY user_id
)
SELECT
    s.user_id,
    COALESCE(confirmation_rate, 0.00) AS confirmation_rate
FROM Signups s
     LEFT JOIN ConfirmationStats c
     USING(user_id);
