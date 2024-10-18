CREATE DATABASE Views;

use Views;
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

-- MySQL Views concept
-- For creating view
CREATE VIEW view1 as
SELECT rollno, name, marks FROM student;

SELECT * FROM view1; 

SELECT * 
FROM view1
WHERE marks > 90;

-- For deleting view
DROP VIEW view1;

SELECT * FROM view1; 