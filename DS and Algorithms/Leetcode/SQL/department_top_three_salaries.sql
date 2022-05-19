SELECT Department, Employee, Salary
FROM 
(

SELECT d.name as Department, e.name as Employee, e.salary as Salary, DENSE_RANK() OVER (PARTITION BY d.name ORDER BY salary DESC) as salary_rank
FROM Employee e JOIN Department d on e.departmentId=d.id

) rnk_table

WHERE rnk_table.salary_rank<4;