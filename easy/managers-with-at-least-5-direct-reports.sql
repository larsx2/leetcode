-- Problem: https://leetcode.com/problems/managers-with-at-least-5-direct-reports/
-- Solution: https://leetcode.com/problems/managers-with-at-least-5-direct-reports/submissions/1012374529/

SELECT m.name
FROM Employee m
  JOIN Employee e
    ON m.id = e.managerId
GROUP BY m.id, m.name -- You can have more than one manager with the same name
HAVING count(e.managerId) >= 5
