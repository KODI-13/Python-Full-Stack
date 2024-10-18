CREATE TABLE customers(
cust_id SERIAL PRIMARY KEY,
cust_name VARCHAR(100) NOT NULL
);

SELECT * FROM customers;



CREATE TABLE orders(
order_id SERIAL PRIMARY KEY,
order_date DATE NOT NULL,
price NUMERIC NOT NULL,
cust_id INTEGER NOT NULL,
FOREIGN KEY (cust_id) REFERENCES
customers (cust_id)
);

SELECT * FROM orders;




INSERT INTO customers
(cust_name)
VALUES
('Raju'),
('Sham'),
('Paul'),
('Alex');

SELECT * FROM customers;


INSERT INTO orders
(order_date, cust_id, price)
VALUES
('2024-01-01', 1, 250.00),
('2024-01-15', 1, 300.00),
('2024-02-01', 2, 150.00),
('2024-03-01', 3, 450.00),
('2024-04-01', 2, 550.00);

SELECT * FROM orders;


-- CROSS JOIN 
-- every row from one table is combined with every rrow in another table
-- so it shows possible ALL outcome
SELECT * FROM customers CROSS JOIN orders;

-- INNER JOIN 
-- matched rows between two column
SELECT * FROM customers c
INNER JOIN 
orders o
ON c.cust_id=o.cust_id;

-- INNER JOIN WITH GROPU BY
-- determining total oders placed by each customer
SELECT c.cust_name, COUNT(o.order_id) FROM customers c
INNER JOIN 
orders o
ON c.cust_id=o.cust_id
group by cust_name;

-- INNER JOIN WITH GROPU BY
-- determining total price paid by each customer
SELECT c.cust_name, SUM(o.price) FROM customers c
INNER JOIN 
orders o
ON c.cust_id=o.cust_id
group by cust_name;


-- LEFT JOIN 
-- ALL DATA FROM LEFT TABLE(THE TABLE U MENTIONED 1ST) AND MATCHED ROW FROM RIGHT TABLE
SELECT * FROM customers c
LEFT JOIN 
orders o
ON c.cust_id=o.cust_id;

-- RIGHT JOIN 
-- ALL DATA FROM RIGHT TABLE(THE TABLE U MENTIONED 2ND) AND MATCHED ROW FROM 1ST TABLE I.E. LEFT
SELECT * FROM customers c
RIGHT JOIN 
orders o
ON c.cust_id=o.cust_id;

-- ===========================================================================================================
-- =========================================
-- go to 4_Many_to_many_Relationship
-- =========================================
-- ===========================================================================================================
