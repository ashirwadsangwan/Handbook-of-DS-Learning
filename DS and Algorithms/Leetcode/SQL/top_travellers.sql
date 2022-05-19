SELECT u.name name, IFNULL(SUM(r.distance), 0) travelled_distance
FROM Users u 
LEFT JOIN  Rides r ON u.id=r.user_id
GROUP BY u.id
ORDER BY travelled_distance DESC, name ASC