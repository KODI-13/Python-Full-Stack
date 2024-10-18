-- listing down the exisiting databases
SELECT datname FROM pg_database;
-- show databases;  doesnot work in postgresql

-- ============================================================================================
-- Creating a New Database 
-- using CMD and using PgAdmin --> CREATE DATABASE <db_name>;
CREATE DATABASE test;

-- ============================================================================================
-- to perform operations in sepearte database 
-- using cmd --> \c <db_name>;
-- using PgAdmin --> simply open query tool while clicking on database name

-- ============================================================================================
-- deleting database 
-- DROP DATABASE <db_name>;     
-- while performing these operation trhough cmd if already in use error occured then using pgadmin try to discooneet these database ur deleting 
DROP DATABASE test;
-- ============================================================================================

-- creating tabale 2nd step i.e. CRAETE TABLE TABLE_NAME(
-- COLOMN_name1 datatype constraints,
-- COLOMN_name2 datatype constraints);

-- create is keyword use to create the table and it define the structure(schema/design) of a table
CREATE TABLE person(
	id INT,
    name VARCHAR(100),
    city VARCHAR(100)
); 

-- to check if that perticular table exists in databse
-- using CMD --> \d <table_name>;
-- using pgadmin --> persondb>Schemas>Tables

-- ============================================================================================================
-- inserting values in the table
-- 1st styntax --> INSERT INTO <table_name>(column_1_name, column_2_name) VALUES(column_1_value,column_2_value);
-- 2nd syntax --> INSERT INTO <table_name> VALUES(column_1_value,column_2_value);
INSERT INTO person
(id, name, city)
VALUES
(102, 'sham', 'mumbai'),
(103, 'paul', 'pune');

-- INSERT INTO person VALUES (104, "sam", "nagpur");   NOT ALLOWED
INSERT INTO person VALUES (104, 'sam', 'nagpur');   -- ALLOWED
INSERT INTO person VALUES (105, 'tryon');  -- ALLOWED

-- ============================================================================================================
-- Showing all data in table format
-- SELECT * FROM <table_name>;
SELECT * FROM person;

-- showing 1, more column in table
SELECT name FROM person;
SELECT name, city FROM person;

-- ============================================================================================================
-- updating values in table 
-- UPDATE <table_name>
-- SET <column_name> = value\'value'
-- WHERE id = 1;

UPDATE person
	SET city = 'banglore'
WHERE 
	id = 105;

SELECT * FROM person;

-- ============================================================================================================
-- deleting data or values in table
-- DELETE FROM <table_name>
-- where <column_name> = vales\'value';

INSERT INTO person VALUES (106, 'tryon');  -- ALLOWED
SELECT * FROM person;

DELETE FROM person
where id = 106;

SELECT * FROM person;

-- ============================================================================================================
-- ===================================
-- go to 2.basic.sql 
-- ===================================
-- ===================================
-- after 2.basic.sql start from here
-- ===================================
-- ============================================================================================================

-- altering table
-- ADDING COLUMN IN EXISTING TABLE
ALTER TABLE person
ADD COLUMN age VARCHAR(50);

-- DROPING COLUMN IN EXISTING TABLE
ALTER TABLE person
DROP COLUMN age;

-- RENAMING COLUMN IN EXISTING TABLE
ALTER TABLE person
RENAME COLUMN name TO fname;

-- RENAMING TABLE ITSELF
ALTER TABLE person
RENAME TO users;

-- setting or changing datatype of a column
ALTER TABLE person
WHERE COLUMN fname
SET DATA TYPE VARCHAR(200);

-- setting default value to a column
ALTER TABLE person
WHERE COLUMN fname
SET DEFAULT 'unknown';

-- DROPING default value to a column
ALTER TABLE person
WHERE COLUMN fname
DROP DEFAULT;

-- setting nullable value of a column to NOT NULL
ALTER TABLE person
WHERE COLUMN fName
SET NOT NULL;

-- DROPING nullable value of a column
ALTER TABLE person
WHERE COLUMN fname
DROP NOT NULL;

-- ADDING COLUMN IN EXISTING TABLE WITH CHECK CONSTRAINT
ALTER TABLE person
ADD COLUMN mob VARCHAR(15)
CHECK (LENGTH(mob)>=10);

INSERT INTO person
(mob)
VALUES
('102');  -- SHOW ERROR BECUSE IT DID NOT PASSED THE CONDITIOIN MENTIOINED IN CHECK CONSTRAINT

INSERT INTO person
(mob)
VALUES
('1234567890'); 

ALTER TABLE person
DROP CONSTRAINT person_mob_check; -- contraint name created automatically can check through cmd using \d person

-- NAMED CONTRAINT
-- AFTER DROPING CONSTRINT ABOVE WE ARE DEFINING CONSTRAINT WITH OUR OWN SPECIFIED NAME
ALTER TABLE person
ADD CONSTRAINT mob_no_less_than_10
CHECK (LENGTH(mob)>=10);

INSERT INTO person
(mob)
VALUES
('102');  -- SHOW ERROR WITH OUR SPECIFIED NAMED CONSTRAINT

INSERT INTO person
(mob)
VALUES
('1234567890'); 

-- ============================================================================================================
-- ===================================
-- go to 2.basic.sql 
-- ===================================
-- ============================================================================================================

