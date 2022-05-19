
-- Approach 1

SELECT id, 
(CASE WHEN p_id IS NULL THEN 'Root'
    WHEN p_id IS NOT NULL AND id IN (SELECT p_id FROM Tree) THEN 'Inner'
    ELSE 'Leaf'
    END
 ) AS type
FROM Tree
ORDER BY id ASC;


-- Approach 2

SELECT * FROM (SELECT id, 'Root' AS type
FROM Tree
WHERE p_id IS NULL

UNION

SELECT id, 'Inner' AS type
FROM Tree
WHERE p_id IS NOT NULL AND id IN (SELECT p_id FROM Tree)

UNION

SELECT id, 'Leaf' AS type
FROM Tree
WHERE p_id IS NOT NULL AND id NOT IN (SELECT p_id FROM Tree WHERE p_id IS NOT NULL)) a

ORDER BY id ASC