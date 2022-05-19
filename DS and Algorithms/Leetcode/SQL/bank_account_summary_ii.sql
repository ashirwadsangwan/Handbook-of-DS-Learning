SELECT a.name as name, b.balance
FROM Users a
LEFT JOIN 
(
    SELECT account, SUM(amount) AS balance
    FROM Transactions
    GROUP BY account
    ) b 
    ON a.account = b.account
WHERE b.balance>10000