-- Problem: https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee/
-- Solution: https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee/submissions/1031030392/

SELECT
  e1.reports_to AS employee_id,
  e2.name AS name,
  COUNT(e1.employee_id) AS reports_count,
  ROUND(AVG(e1.age)) AS average_age
  FROM Employees e1
  JOIN Employees e2
    ON e1.reports_to = e2.employee_id
  GROUP BY e1.reports_to
  ORDER BY e1.reports_to
