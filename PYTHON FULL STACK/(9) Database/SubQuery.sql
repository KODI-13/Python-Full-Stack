CREATE DATABASE subquery;
use subquery;
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
(102, "bumika", 93, "A", "Mumbai"),
(103,"chetan", 85, "B", "Mumbai"),
(104, "dhurv", 96, "A", "Delhi"),
(105, "farah", 82, "B", "Delhi");

SELECT * FROM student;

SELECT AVG(marks)
FROM student;

SELECT name, marks
FROM student
WHERE marks > 86.8000;

-- subquery concept
-- query for above two queries
-- find the name of student whoes marks are greater than avg of class
SELECT name, marks
FROM student
WHERE marks > (SELECT AVG(marks) FROM student);

-- find the name of of student with even roll number
SELECT rollno -- , name
FROM student 
where rollno % 2 = 0 ;

SELECT name, rollno
FROM student 
where rollno IN (102, 104);

-- query for above two queries
SELECT name, rollno
FROM student 
where rollno IN (
	SELECT rollno 
	FROM student 
	where rollno % 2 = 0 );
    
-- Subquery inside fROM (*NOTE = use of subquery inside from then it needs to be assign with alis)
-- Find the maximum marks from the students of delhi 
SELECT *
FROM student
WHERE city = "Delhi";

SELECT MAX(marks)
FROM (SELECT * FROM student WHERE city = "Delhi") as tem;

-- the another way to do above query without using subquery
SELECT MAX(marks)
FROM student
WHERE city = "Mumbai";

-- Subquery inside SELECT
SELECT (SELECT MAX(marks) FROM student), name
FROM student;

SELECT (SELECT marks FROM student), name
FROM student;