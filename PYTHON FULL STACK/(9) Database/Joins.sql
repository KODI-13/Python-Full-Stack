CREATE DATABASE IF NOT EXISTS Joins; 
USE Joins;

CREATE TABLE student(
id INT PRIMARY KEY,
name VARCHAR(50)
);

INSERT INTO student 
(id, name)
VALUES
(101, "adam"),
(102, "bob"),
(103, "casey");

CREATE TABLE course(
id INT PRIMARY KEY,
course VARCHAR(50)
);

INSERT INTO course 
(id, course)
VALUES
(102, "english"),
(105, "math"),
(103, "science"),
(107, "computer science");

SELECT * FROM student;
SELECT * FROM course;

-- inner join syntax
SELECT *
FROM student as s 
INNER JOIN course as c
ON s.id = c.id;

-- Left outer join
SELECT *
FROM student as s 
LEFT JOIN course as c
ON s.id = c.id;

-- Right outer join
SELECT *
FROM student as s 
RIGHT JOIN course as c
ON s.id = c.id;

-- Full outer join
SELECT *
FROM student as s 
LEFT JOIN course as c
ON s.id = c.id
UNION
SELECT *
FROM student as s 
RIGHT JOIN course as c
ON s.id = c.id;

-- Left Exclusive join
SELECT *
FROM student as s 
LEFT JOIN course as c
ON s.id = c.id
WHERE c.id IS NULL;

-- Right Exclusive join
SELECT *
FROM student as s 
RIGHT JOIN course as c
ON s.id = c.id
WHERE s.id IS NULL;

-- Full Exzclusive join
SELECT *
FROM student as s 
LEFT JOIN course as c
ON s.id = c.id
WHERE s.id AND c.id IS NOT NULL
UNION
SELECT *
FROM student as s 
RIGHT JOIN course as c
ON s.id = c.id
WHERE s.id AND c.id IS NOT NULL;


-- self join 
CREATE TABLE employee(
id INT PRIMARY KEY,
name VARCHAR(50),
manager_id INT
);

INSERT INTO employee
(id, name, manager_id)
VALUES
(101,"adam",103),
(102,"bob",104),
(103,"casey", NULL),
(104,"donald",103);

SELECT * FROM employee;

SELECT *
FROM employee as a
JOIN employee as b
ON a.id = b.manager_id;

SELECT a.name as manager_name, b.name
FROM employee as a
JOIN employee as b
ON a.id = b.manager_id;

-- Union concept 
-- UNION remove duplicates and returjn unique values
-- UNION ALL does not remove duplicates i.e. it returns duplicates also
SELECT name FROM employee
UNION
SELECT name FROM employee;

SELECT name FROM employee
UNION ALL
SELECT name FROM employee;