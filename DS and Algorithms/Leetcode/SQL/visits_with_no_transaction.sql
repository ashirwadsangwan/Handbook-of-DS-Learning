SELECT (customer_id), COUNT(visit_id) count_no_trans
FROM Visits
WHERE visit_id NOT in (SELECT visit_id FROM Transactions)
GROUP BY customer_id