SELECT d.name as "Department", e.name as "Employee", e.salary as "Salary"
FROM Employee e
JOIN Department d ON e.departmentId = d.id
WHERE e.salary >= (SELECT MIN(salary) FROM (
    SELECT salary
    FROM Employee
    WHERE departmentId = d.id
    GROUP BY salary
    ORDER BY salary DESC
    LIMIT 3
))