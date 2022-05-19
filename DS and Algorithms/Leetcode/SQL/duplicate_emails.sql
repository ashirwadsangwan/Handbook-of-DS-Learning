SELECT email from (
    SELECT EMAIL, COUNT(EMAIL) AS num
    FROM Person
    GROUP BY EMAIL
) as statistic where num >=2;