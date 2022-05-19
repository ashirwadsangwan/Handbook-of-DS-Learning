-- If we know all the persons who have sales in this company 'RED', it will be fairly easy to know who do not have.
SELECT s.name
FROM salesperson s
WHERE s.sales_id NOT IN 

    (SELECT
        o.sales_id
    FROM
        orders o
            LEFT JOIN
        company c ON o.com_id = c.com_id
    WHERE
        c.name = 'RED'
        ) 