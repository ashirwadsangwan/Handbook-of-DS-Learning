SELECT actor_id, director_id
FROM (
    SELECT actor_id, director_id, count(*) num
    FROM ActorDirector
    GROUP BY 1, 2
    ) a
WHERE a.num>2