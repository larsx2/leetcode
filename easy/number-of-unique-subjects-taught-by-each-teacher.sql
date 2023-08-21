-- Problem: https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher/
-- Solution: https://leetcode.com/submissions/detail/1026171879/

SELECT
    teacher_id,
    COUNT(DISTINCT subject_id) AS cnt
FROM Teacher
GROUP BY teacher_id
