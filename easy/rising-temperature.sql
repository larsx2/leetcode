-- Problem: https://leetcode.com/problems/rising-temperature/
-- Solution: https://leetcode.com/submissions/detail/1011764319/
SELECT id
FROM (
  SELECT
    id,
    temperature,
    LAG(temperature, 1)
      OVER (ORDER BY recordDate) AS prevTemperature,
    recordDate,
    LAG(recordDate, 1)
      OVER (ORDER BY recordDate) AS prevDate
  FROM Weather
) AS sq
WHERE
    temperature > prevTemperature
    AND DATEDIFF(recordDate, prevDate) = 1
