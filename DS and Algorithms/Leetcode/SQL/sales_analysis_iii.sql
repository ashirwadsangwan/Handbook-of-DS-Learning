SELECT p.product_id, p.product_name
FROM product p
WHERE p.product_id NOT IN (SELECT product_id
                          FROM Sales 
                          WHERE sale_date>'2019-03-31' OR sale_date<'2019-01-01')