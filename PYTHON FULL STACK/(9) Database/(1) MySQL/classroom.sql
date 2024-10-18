-- -- creating a database
-- CREATE DATABASE tem1;

-- -- Deleting a database
-- DROP DATABASE tem1;
-- DROP DATABASE tem2;
-- create database tem2;

-- best practice when deleting a database (*NOTE = use of "IF EXISTS" keyword does not give us any error ..it just show us a warning) 
DROP DATABASE IF EXISTS company;
-- Creating a database
CREATE DATABASE college;

-- best practice when creating a database (*NOTE = use of "IF NOT EXISTS" keyword does not give us any error ..it just show us a warning) 
CREATE DATABASE IF NOT EXISTS college;

-- creating table 1st step i.e. use db_name
USE college;

-- creating tabale 2nd step i.e. CRAETE TABLE TABLE_NAME(
-- COLOMN_name1 datatype constraints,
-- COLOMN_name2 datatype constraints);

-- create is keyword use to create the table and it define the structure(schema/design) of a table
CREATE TABLE student(
	id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT NOT NULL
); 

-- as you can drop the table also 
DROP TABLE student;

-- inserting values in the table
INSERT INTO student VALUES(1,"DEEP",20);
INSERT INTO student VALUES(2,"SIDHHI",21);

-- Showing all data in table format
SELECT * FROM student;

-- To show all databses 
SHOW DATABASES;

-- To show all tables in the use databses (*NOTE = use database means the database we are working right now)
SHOW TABLES;

CREATE TABLE student(
rollno INT PRIMARY KEY,
NAME VARCHAR(50)
);

SELECT * FROM student;

INSERT INTO student
(rollno, NAME)
 values
 (1,"deepak"),
 (2,"SIDDHI");
 
 CREATE DATABASE XYZ;
 USE XYZ;
 
 CREATE TABLE employee(
	id INT PRIMARY KEY,
    name VARCHAR(50),
    salary INT
 );
 
 INSERT INTO employee
(id, name, salary)
 values
 (1,"adam",25000),
 (2,"bob",30000),
 (3,"casey",40000);
 
 SELECT * FROM employee;
 
 use college;
 -- another syntax of using primary key and with the helpof this u can make combination of two columns as primary key
  CREATE TABLE tem1(
	id INT,
    name VARCHAR(50),
    age INT,
    city VARCHAR(20),
    PRIMARY KEY(id, name)
 );
 
  CREATE TABLE emp(
	id INT PRIMARY KEY,
    salary INT DEFAULT 25000
 );
 
 INSERT INTO emp (id) values (101);
  SELECT * FROM emp;
 

