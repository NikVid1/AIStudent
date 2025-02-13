-- Select all employees
SELECT * FROM employees;
-- Select specific columns
SELECT name, salary FROM employees;
-- Select all employees with a salary greater than 50000
SELECT * FROM employees WHERE salary > 50000;
-- Select all employees with a name that is not null
SELECT * FROM employees WHERE name IS NOT NULL;
-- Select all employees ordered by salary in descending order
SELECT * FROM employees ORDER BY salary DESC;
-- Count the number of employees
SELECT COUNT(*) FROM employees;
-- Select the average salary by department
SELECT department, AVG(salary) FROM employees GROUP BY department;
-- Select all employees and their departments
SELECT * FROM employees e
JOIN departments d ON e.department_id = d.id;