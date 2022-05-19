SELECT player_id, min(event_date) first_login
FROM Activity
GROUP BY player_id