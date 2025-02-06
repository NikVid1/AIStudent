SELECT 
    s.product_id,
    (SUM(s.sales) * p.price) AS total_revenue
FROM sales AS s
JOIN pricing AS p ON s.product_id = p.product_id
GROUP BY s.product_id, p.price;
