DELETE FROM PERSON WHERE id not in (

SELECT * FROM (SELECT MIN(id) FROM Person GROUP BY Email) AS p)