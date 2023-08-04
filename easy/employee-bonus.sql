-- Problem: https://leetcode.com/problems/employee-bonus/
-- Solution: https://leetcode.com/submissions/detail/1011786707/
SELECT name, bonus
FROM Bonus RIGHT JOIN Employee
  USING (empId)
WHERE bonus is NULL or bonus < 1000;
