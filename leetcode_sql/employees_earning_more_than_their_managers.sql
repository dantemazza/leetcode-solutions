# Write your MySQL query statement below
SELECT Name as Employee FROM (
    WITH A as (SELECT * FROM Employee), B as (SELECT * FROM Employee) SELECT B.Name, B.Salary, A.Salary as MSalary FROM A INNER JOIN B on A.Id = B.ManagerId
    ) AS T WHERE Salary > MSalary;
