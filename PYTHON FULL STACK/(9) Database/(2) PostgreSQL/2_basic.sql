CREATE TABLE employees(
emp_id SERIAL PRIMARY KEY,
fname VARCHAR(100) NOT NULL,
lname VARCHAR(100) NOT NULL,
email VARCHAR(200) NOT NULL UNIQUE,
dept VARCHAR(100),
salary DECIMAL(10,2) DEFAULT 30000.00,
hire_date DATE NOT NULL DEFAULT CURRENT_DATE
);

INSERT INTO employees 
(emp_id, fname, lname, email, dept, salary, hire_date) 
VALUES
(1, 'Raj', 'Sharma', 'raj.sharma@example.com', 'IT', 50000.00, '2020-01-15'),
(2, 'Priya', 'Singh', 'priya.singh@example.com', 'HR', 45000.00, '2019-03-22'),
(3, 'Arjun', 'Verma', 'arjun.verma@example.com', 'IT', 55000.00, '2021-06-01'),
(4, 'Suman', 'Patel', 'suman.patel@example.com', 'Finance', 60000.00, '2018-07-30'),
(5, 'Kavita', 'Rao', 'kavita.rao@example.com', 'HR', 47000.00, '2020-11-10'),
(6, 'Amit', 'Gupta', 'amit.gupta@example.com', 'Marketing', 52000.00, '2020-09-25'),
(7, 'Neha', 'Desai', 'neha.desai@example.com', 'IT', 48000.00, '2019-05-18'),
(8, 'Rahul', 'Kumar', 'rahul.kumar@example.com', 'IT', 53000.00, '2021-02-14'),
(9, 'Anjali', 'Mehta', 'anjali.mehta@example.com', 'Finance', 61000.00, '2018-12-03'),
(10, 'Vijay', 'Nair', 'vijay.nair@example.com', 'Marketing', 50000.00, '2020-04-19');

SELECT * FROM employees;


-- checking all constraintes
INSERT INTO employees 
(fname, lname, email, dept) 
VALUES
('kajal', 'Mehta', 'kajal.mehta@example.com', 'Finance');

SELECT * FROM employees;

--above checking contraints query will give error .... to solve these do following steps
-- ERROR:  Key (emp_id)=(1) already exists.duplicate key value violates unique constraint "employees_pkey" 

-- ERROR:  duplicate key value violates unique constraint "employees_pkey"
-- SQL state: 23505
-- Detail: Key (emp_id)=(1) already exists.

SELECT SETVAL('employees_emp_id_seq', 10);

SELECT CURRVAL('employees_emp_id_seq');

-- after solving above error you can try again follwing queries
-- checking all constraintes
INSERT INTO employees 
(fname, lname, email, dept) 
VALUES
('kajal', 'Mehta', 'kajal.mehta@example.com', 'Finance');

SELECT * FROM employees;

-- lets checkj again if sequence is started or not
INSERT INTO employees 
(fname, lname, email, dept) 
VALUES
('payal', 'Mehta', 'payal.mehta@example.com', 'Finance');

SELECT * FROM employees;

-- ===========================================================================================================
-- DATA REFINING
SELECT * FROM employees;


SELECT * FROM employees
WHERE dept = 'HR';


SELECT * FROM employees
WHERE salary >= 50000;


SELECT * FROM employees
WHERE dept='HR' OR dept='IT';


SELECT * FROM employees
WHERE SALARY>50000 AND dept='IT';


SELECT * FROM employees
WHERE dept IN ('HR','IT', 'Marketing');


SELECT * FROM employees
WHERE dept NOT IN ('HR','IT');


SELECT * FROM employees
WHERE SALARY BETWEEN 50000 AND 60000;


SELECT dept FROM employees;

SELECT DISTINCT dept FROM employees;


SELECT * FROM employees
ORDER BY fname;


SELECT * FROM employees
ORDER BY fname DESC;


SELECT * FROM employees LIMIT 3;


SELECT * FROM employees
WHERE fname LIKE 'A%';


SELECT * FROM employees
WHERE fname LIKE '%a';


SELECT * FROM employees
WHERE fname LIKE '%i%';


SELECT * FROM employees
WHERE dept LIKE '__';


SELECT * FROM employees
WHERE fname LIKE '_a%';


SELECT * FROM employees
WHERE lname LIKE '%h__';


-- AGGREGATE FUNCTIONS
SELECT COUNT(emp_id) FROM employees;   -- USE PRIMARY KEY IN ORDER TO FIND COUNT BECAUSEE IT DOES NOT CONTAIN NULL VALUE

SELECT COUNT(fname) FROM employees;

SELECT SUM(salary) FROM employees;

SELECT AVG(salary) FROM employees;

SELECT MIN(salary) FROM employees;

SELECT MAX(salary) FROM employees;



-- GROUP BY CLAUSE
SELECT dept FROM employees GROUP BY dept;

SELECT dept, COUNT(emp_id) FROM employees GROUP BY dept;

SELECT dept, SUM(salary) FROM employees GROUP BY dept;



-- STRING FUNCATIONS -- USEFUL WHEN WE HAVE TO WORK ON VALUES OF TABLE .. WORK ON MEANS PERFORMING OPERATIONS LIKE MANUPULATION, DECORATION
SELECT CONCAT('Hello', 'World');

SELECT CONCAT(fname, lname) FROM employees;

SELECT CONCAT(fname, lname) AS FullName FROM employees;

SELECT emp_id, CONCAT(fname, lname) AS FullName, dept FROM employees;

SELECT emp_id, CONCAT(fname, ' ', lname) AS FullName, dept FROM employees;


-- CONCATE WITH SEPARATOR
SELECT CONCAT_WS(':', 'One', 'Two', 'Three');

SELECT CONCAT_WS('-', 'One', 'Two', 'Three');

SELECT emp_id, CONCAT_WS(' ', fname, lname) AS FullName, dept FROM employees;



-- SUBSTRING 
SELECT SUBSTRING('HELLO WORLD!', 1,5);		-- 1ST WAY TO USE

SELECT SUBSTR('HELLO WORLD!', 1,4);        -- 2NDWAY TO USE



-- REPLACE
SELECT REPLACE('HELLO WORLD!', 'HELLO', 'HEY');

SELECT REPLACE(dept, 'IT', 'Tech') FROM employees;

SELECT REPLACE(dept,'Tech', 'IT') FROM employees;



-- REVERSE
SELECT REVERSE('HELLO');

SELECT REVERSE(fname) FROM employees;



-- LENGTH
SELECT LENGTH('HELLO');

SELECT LENGTH(fname) FROM employees;

SELECT * FROM employees 
WHERE LENGTH(fname) > 5;



-- UPPER AND LOWER
SELECT UPPER(fname) FROM employees;

SELECT LOWER(fname) FROM employees;



-- LEFT, RIGHT AND TRIM
SELECT LEFT('HELLO WORLD!', 4);

SELECT RIGHT('HELLO WORLD!', 6);

SELECT LENGTH('    ALRIGHT   ');

SELECT LENGTH(TRIM('    ALRIGHT   '));



-- POSITION 
SELECT POSITION('OM' IN 'THOMAS');


-- ===========================================================================================================
-- EXERCISE ON ABOVE THING
SELECT CONCAT_WS(':', emp_id, fname, lname, dept) FROM employees
WHERE emp_id = 1;

SELECT CONCAT_WS(':', emp_id, CONCAT_WS(' ',fname, lname), dept) FROM employees
WHERE emp_id = 1;

SELECT CONCAT_WS(':', emp_id, fname, UPPER(dept)) FROM employees
WHERE emp_id = 4;

SELECT CONCAT(LEFT(dept, 1), emp_id), fname FROM employees;


-- ===========================================================================================================
-- SUBQUERY
SELECT * FROM employees
where 
salary = (SELECT MAX(salary) FROM employees);

SELECT * FROM employees
where 
salary = (SELECT MIN(salary) FROM employees);

-- ===========================================================================================================
-- ===================================
-- go to 1.basic.sql 
-- ===================================
-- ===================================
-- after 1.basic.sql start from here
-- ===================================
-- ============================================================================================================

-- altering table
-- CASE EXPRESSION
SELECT Fname, salary,	-- COMMA IS IMPORTANT HERE
CASE
	WHEN salary >= 50000 THEN 'HIGH'
	ELSE 'LOW
END AS sal_cat'
FROM employees;


SELECT Fname, salary,	-- COMMA IS IMPORTANT HERE
CASE
	WHEN salary >= 55000 THEN 'HIGH'
	WHEN salary BETWEEN 48000 AND 55000 THEN 'MID'
	ELSE 'LOW'
END AS sal_cat
FROM employees;

-- GIVING BONUS 10% PERCENT OF SALARY
SELECT Fname, salary,	-- COMMA IS IMPORTANT HERE
CASE
	WHEN salary >= 0 THEN salary*0.10
END AS bonus
FROM employees;

-- GIVING BONUS 10% PERCENT OF SALARY WITH ROUND OF FUNCTION
SELECT Fname, salary,	-- COMMA IS IMPORTANT HERE
CASE
	WHEN salary >= 0 THEN ROUND(salary*0.10)
END AS bonus
FROM employees;

-- CASE EXPRESSION WITH GROUP BY
SELECT              -- COMMA IS NOT NECCESSARY HERE
CASE
	WHEN salary >= 55000 THEN 'HIGH'
	WHEN salary BETWEEN 48000 AND 55000 THEN 'MID'
	ELSE 'LOW'
END AS sal_cat, COUNT(emp_id)
FROM employees
GROUP BY sal_cat;

-- ===========================================================================================================
-- ====================================================
-- go to 3_relationship_1_to_many_and_join
-- ====================================================

-- ====================================================
-- after 5_many_to_many_and_view.sql start from here
-- ====================================================
-- ===========================================================================================================


-- All comes under stored procedure until equal to comment
SELECT * FROM employees;

UPDATE employees
SET salary = 97000
WHERE emp_id = 4;

-- STORED PROCEDURE 
-- WHEN WE HAVE TO USE ONE QUERY MULTIPLE TIMES THEN WE STORE THAN QUERY OR QUERIES INTO DATABASE
CREATE OR REPLACE PROCEDURE update_emp_salary (
	p_employee_id INT,
	p_new_salary NUMERIC 
)
LANGUAGE plpgsql
AS $$
BEGIN 
	UPDATE employees
	SET salary = p_new_salary
	WHERE emp_id = p_employee_id;
END;
$$;


CALL update_emp_salary(3, 71000);



-- ===========================================================================================

SELECT * FROM employees;

-- FINDING THE FULL DETAILS OF AN EMPLOYEE WITH MAX SALARY IN EACH DEPARTMENT 
SELECT dept, MAX(SALARY)		-- THIS QUERY WILL NOT GIVE THE FULL DETAILS OF EMPLOYEE SO WE ARE GOING TO USE FOLLOWING SUBQUERY 
FROM employees
GROUP BY dept;

-- SUBQUERY TO PRINT FULL DETAILS OF AN EMPLOYEE WITH MAX SALARY IN EACH DEPARTMENT 
SELECT *
FROM employees
WHERE dept = 'HR' 
     AND salary = (
	 	SELECT MAX(salary)
		FROM employees
		WHERE dept = 'HR'
	);


-- CREATING A USER DEFINED FUNCTION WHICH WILL GIVE ALL DETAILS OF AN EMPLOYEE WITH WITH MAX SSALARY IN PERTICULAR DEPARTMENT
CREATE OR REPLACE FUNCTION dept_max_sal_emp1(dept_name VARCHAR)
RETURNS TABLE(emp_id INT, fname VARCHAR, salary NUMERIC) 
AS $$
BEGIN
    RETURN QUERY
    SELECT 
        e.emp_id,  e.fname, e.salary
    FROM 
        employees e
    WHERE 
        e.dept = dept_name
        AND e.salary = (
            SELECT MAX(emp.salary)
            FROM employees emp
            WHERE emp.dept = dept_name
        );
END;
$$ LANGUAGE plpgsql;


SELECT * FROM dept_max_sal_emp1('HR');
SELECT * FROM dept_max_sal_emp1('IT');



-- =========================================================================================================================================================
-- WINDOWS FUNCTION 
SELECT fname, 
		SUM(salary) OVER()   -- add new column where each row contain sum of salary
		FROM employees;

SELECT fname, salary,
		SUM(salary) OVER()
		FROM employees;

SELECT fname, salary,
		SUM(salary) OVER(ORDER BY salary)	-- add new column where sum of salary in each row is ascending according to order of salary 
		FROM employees;						-- running increasing salary total

SELECT fname, salary,
		AVG(salary) OVER(ORDER BY salary)   -- add new column with running average
		FROM employees;

SELECT ROW_NUMBER() OVER(),  -- COMMA IS IMPORTANT HERE
		fname, dept, salary
		FROM employees;

SELECT ROW_NUMBER() OVER(ORDER BY fname),  -- COMMA IS IMPORTANT HERE
		fname, dept, salary
		FROM employees;

SELECT ROW_NUMBER() OVER(PARTITION BY dept),  -- PARTITIION BY WORK AS GROUP BY
		fname, dept, salary
		FROM employees;

SELECT fname, salary,
		RANK() OVER(ORDER BY salary)
		FROM employees;

SELECT fname, salary,
		DENSE_RANK() OVER(ORDER BY salary)
		FROM employees;


SELECT fname, salary,
		DENSE_RANK() OVER(ORDER BY salary DESC)
		FROM employees;


SELECT fname, salary,
		LAG(salary) OVER()
		FROM employees;

SELECT fname, salary,
		LEAD(salary) OVER()
		FROM employees;

SELECT fname, salary,
		LEAD(salary) OVER(ORDER BY salary)
		FROM employees;


SELECT fname, salary,
		LEAD(salary) OVER(ORDER BY salary DESC)
		FROM employees;

SELECT fname, salary,
		(salary - LEAD(salary) OVER(ORDER BY salary DESC))
		FROM employees;



-- =========================================================================================================================================================
-- CTE (Common Table Expression)
-- show the avg salary in each department and the data of an employee with greater salary than avg salary
WITH avg_sal AS (
	SELECT dept, AVG(salary) as avg_salary FROM employees GROUP BY dept
)
SELECT
	e.emp_id, e.fname, e.dept, e.salary, a.avg_salary
FROM employees e
JOIN avg_sal a ON e.dept = a.dept
WHERE e.salary > a.avg_salary;


-- find the highest paid employee in each department
WITH max_sal AS (
	SELECT dept, MAX(salary) AS max_salary FROM employees GROUP BY dept
)
SELECT 
	e.emp_id, e.fname, e.dept, e.salary
FROM employees e
JOIN max_sal m ON e.dept = m.dept
WHERE e.salary = m.max_salary;




-- =========================================================================================================================================================
-- Triggers
-- 1st step create function 
SELECT * FROM employees;

CALL update_emp_salary(1, -52000);	-- before creating following function we can use this one but after creation of below function it will assign 0 to negative values

-- writing logic for trigger in a function in which if any negative value is inserted or updated then it will make it as 0
CREATE OR REPLACE FUNCTION check_salary()
RETURNS TRIGGER
AS $$
BEGIN 
	IF NEW.salary< 0 THEN
		NEW.salary = 0;
	END IF;
	RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER before_update_salary
BEFORE UPDATE ON employees
FOR EACH ROW
EXECUTE FUNCTION check_salary();

CALL update_emp_salary(2, -52000);	-- after creation of above function it will assign 0 to negative values

SELECT * FROM employees;

-- =========================================================================================================================================================

-- ENDS HERE 