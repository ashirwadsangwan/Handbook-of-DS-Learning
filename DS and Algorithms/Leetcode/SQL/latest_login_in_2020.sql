SELECT user_id, time_stamp as last_stamp
FROM

    (SELECT *, rank() OVER (PARTITION BY user_id ORDER BY time_stamp DESC) as rnk
    FROM Logins 
    WHERE YEAR(time_stamp)=2020) a
    
WHERE a.rnk=1