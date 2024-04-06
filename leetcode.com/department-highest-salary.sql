SELECT d.name as Department, e.name as Employee, e.Salary
FROM Department d
JOIN (
    SELECT name, salary, departmentId
    FROM Employee ee
    WHERE salary = (
        SELECT MAX(salary)
        FROM Employee eee
        WHERE ee.departmentId = eee.departmentId
        GROUP BY eee.departmentId
    )
) e ON d.id = e.departmentId