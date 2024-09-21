CREATE DATABASE school;
use school;
CREATE TABLE student(
rollno INT PRIMARY KEY,
name VARCHAR(50),
marks INT NOT NULL,
grade VARCHAR(1),
city VARCHAR(20)
);

INSERT INTO student
(rollno, name, marks, grade, city)
values
(101, "anil",78, "C","Pune"),
(102, "numika", 93, "A", "Mumbai"),
(103,"chetan", 85, "B", "Mumbai"),
(104, "dhurv", 96, "A", "Delhi"),
(105, "farah", 82, "B", "Delhi");

SELECT name, marks FROM student;
SELECT city FROM student;
SELECT DISTINCT city FROM student; -- Distinct shows unique values in the selected column

-- SELECT with WHERE clause
SELECT * FROM student WHERE marks>85;
SELECT * FROM student WHERE city="Mumbai";

-- SELECT with WHERE clause and using operators
SELECT * FROM student WHERE marks>85 AND city="Mumbai"; 
SELECT * FROM student WHERE marks>85 OR city="Mumbai";
SELECT * FROM student WHERE marks BETWEEN 80 AND 90;
SELECT * FROM student WHERE city IN ("Mumbai", "Delhi", "Punjab");
SELECT * FROM student WHERE city NOT IN ("Mumbai", "Delhi");

-- SELECT with LIMIT clause
SELECT * FROM student LIMIT 3;

-- SELECT with WHERE and LIMIT clause (i.e. using LIMIT clause on WHERE clause) 
SELECT * FROM student WHERE marks>85 LIMIT 3;

-- SELECT with ORDER BY clause
SELECT * FROM student ORDER BY city ASC;
SELECT * FROM student ORDER BY marks ASC;
SELECT * FROM student ORDER BY marks DESC LIMIT 3;

-- SELECT with Aggregate Functions
SELECT MAX(marks) FROM student;
SELECT MIN(marks) FROM student; 
SELECT AVG(marks) FROM student; 
SELECT COUNT(rollno) FROM student; 

-- SELECT with GROUP BY clause 
SELECT city, COUNT(rollno)
FROM student
GROUP BY city;

SELECT city, AVG(marks)
FROM student
GROUP BY city;

SELECT city, AVG(marks)
FROM student
GROUP BY city
ORDER BY AVG(marks);

SELECT city, AVG(marks)
FROM student
GROUP BY city
ORDER BY AVG(marks) DESC;

SELECT grade, COUNT(rollno)
FROM student
GROUP BY grade
ORDER BY grade;

-- select with Having Clause
SELECT city, COUNT(rollno)
FROM student
GROUP BY city
HAVING MAX(marks) > 90;

SELECT city
FROM student
WHERE grade = "A";

SELECT city
FROM student
WHERE grade = "A"
GROUP BY city
HAVING MAX(marks) > 93;

SELECT city
FROM student
WHERE grade = "A"
GROUP BY city
HAVING MAX(marks) >= 93
ORDER BY city DESC;

-- Table related queries
-- How to update data in table
-- First you have to deactivate safe mode in order to update data using following command
SET SQL_SAFE_UPDATES = 0; -- To deactivate safe mode

SET SQL_SAFE_UPDATES = 1; -- To activate safe mode

UPDATE student
SET grade = "O"
WHERE grade = "A";

SELECT * FROM student;

UPDATE student
SET name = "bhumika"
WHERE rollno = 102;

SELECT * FROM student;

UPDATE student
SET marks = marks + 1;

SELECT * FROM student;

-- Deleting data from table
INSERT INTO student VALUES(106,"JOHN", 12, "F", "Delhi");
SELECT * FROM student;

DELETE FROM student 
WHERE marks<33;

SELECT * FROM student;

-- Foreign key concept
CREATE TABLE dept(
id INT PRIMARY KEY,
name VARCHAR(50)
);

CREATE TABLE teacher(
id INT PRIMARY KEY,
name VARCHAR(50),
dept_id INT,
FOREIGN KEY (dept_id) REFERENCES dept(id)
);

-- To visualize above thing we have eer digram for that you have to go from databases --> reverse engineer --> selectg databseand execute and finish
-- EER a.k.a ER digram shows how multiple tables in databases are connected