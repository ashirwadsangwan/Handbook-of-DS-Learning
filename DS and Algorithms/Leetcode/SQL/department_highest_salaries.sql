
SELECT d.name AS Department, e.name AS Employee, Salary
FROM Employee e
LEFT JOIN Department d ON e.departmentId=d.id

WHERE (DepartmentId, Salary) IN (SELECT
                                        DepartmentId, MAX(Salary) 
                                    FROM
                                        Employee 
                                    GROUP BY DepartmentId)