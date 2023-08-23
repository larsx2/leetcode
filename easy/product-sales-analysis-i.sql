-- Problem: https://leetcode.com/problems/product-sales-analysis-i/
-- Solution: https://leetcode.com/submissions/detail/1008110275/

SELECT
    p.product_name,
    s.year,
    s.price
FROM Sales s JOIN Product p
  USING (product_id)
