-- Problem: https://leetcode.com/problems/product-sales-analysis-iii/
-- Solution: https://leetcode.com/submissions/detail/1027284737/

SELECT
    product_id,
    year AS first_year,
    quantity,
    price
FROM (
    SELECT *, RANK() OVER (PARTITION BY product_id ORDER BY year) AS ranking
    FROM Sales
) AS q
WHERE ranking = 1
