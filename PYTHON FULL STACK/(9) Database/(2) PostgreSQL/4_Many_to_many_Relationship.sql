CREATE TABLE students (
s_id SERIAL PRIMARY KEY,
name VARCHAR(100) NOT NULL
);

SELECT * FROM students;


CREATE TABLE courses (
c_id SERIAL PRIMARY KEY,
name VARCHAR(100) NOT NULL,
fee NUMERIC NOT NULL
);

SELECT * FROM courses;


CREATE TABLE enrollment (
enrollment_id SERIAL PRIMARY KEY,
s_id INT NOT NULL,
c_id INT NOT NULL,
enrollment_date DATE NOT NULL,
FOREIGN KEY (s_id) REFERENCES students(s_id),
FOREIGN KEY (c_id) REFERENCES courses(c_id)
);

SELECT * FROM enrollment;


INSERT INTO students
(name)
VALUES
('Raju'),
('Sham'),
('Alex');

SELECT * FROM students;

INSERT INTO courses
(name, fee)
VALUES
('Maths', 500.00),
('Physics', 600.00),
('Chemistry', 700.00);

SELECT * FROM courses;


INSERT INTO enrollment
(s_id, c_id, enrollment_date)
VALUES
(1, 1, '2024-01-01'),   -- Raju enrolled in mathematics
(1, 2, '2024-01-15'),   -- Raju enrolled in Physics
(2, 1, '2024-02-01'),   -- sham enrolled in mathematics
(2, 3, '2024-02-15'),   -- sham enrolled in Chemistry
(3, 3, '2024-03-25');   -- sham enrolled in Chemistry

SELECT * FROM enrollment;


SELECT s.name AS Student_name,
	   c.name AS Course_name,
	   e.enrollment_date,
	   c.fee
FROM enrollment e
JOIN students s ON e.s_id = s.s_id
JOIN courses c ON e.c_id = c.c_id;

-- ===========================================================================================
-- ==================================
-- go to 5_many_to_many_and_view.sql
-- ==================================
-- ===========================================================================================

