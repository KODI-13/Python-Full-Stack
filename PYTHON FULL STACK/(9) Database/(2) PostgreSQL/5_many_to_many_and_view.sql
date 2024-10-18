CREATE TABLE customers (
    cust_id SERIAL PRIMARY KEY,
    cust_name VARCHAR(100) NOT NULL
);

INSERT INTO customers
(cust_name)
VALUES
('Raju'),
('Sham'),
('Paul'),
('Alex');

SELECT * FROM customers;



CREATE TABLE orders (
    ord_id SERIAL PRIMARY KEY,
    ord_date DATE NOT NULL,
    cust_id INTEGER NOT NULL,
    FOREIGN KEY (cust_id) REFERENCES customers(cust_id)
);

INSERT INTO orders 
(ord_date, cust_id)
VALUES
('2024-01-01', 1),  -- Raju first order
('2024-02-01', 2),  -- Sham first order
('2024-03-01', 3),  -- Paul first order
('2024-04-04', 2);  -- Sham second order

SELECT * FROM orders;



CREATE TABLE products (
    p_id SERIAL PRIMARY KEY,
    p_name VARCHAR(100) NOT NULL,
    price NUMERIC NOT NULL
);

INSERT INTO products 
(p_name, price)
VALUES
('Laptop', 55000.00),
('Mouse', 500),
('Keyboard', 800.00),
('Cable', 250.00);

SELECT * FROM products;




CREATE TABLE order_items (
    item_id SERIAL PRIMARY KEY,
    ord_id INTEGER NOT NULL,
    p_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    FOREIGN KEY (ord_id) REFERENCES orders(ord_id),
    FOREIGN KEY (p_id) REFERENCES products(p_id)
);

INSERT INTO order_items
(ord_id, p_id, quantity)
VALUES
(1, 1, 1),  -- Raju ordered 1 Laptop
(1, 4, 2),  -- Raju ordered 2 Cables
(2, 1, 1),  -- Sham ordered 1 Laptop
(3, 2, 1),  -- Paul ordered 1 Mouse
(3, 4, 5),  -- Paul ordered 5 Cables
(4, 3, 1);  -- Sham ordered 1 Keyboard

SELECT * FROM order_items;



SELECT 
	c.cust_name,
	o.ord_date,
	p.p_name,
	p.price,
	oi.quantity,
	(oi.quantity*p.price) AS total_price
FROM order_items oi
	JOIN
		products p ON oi.p_id=p.p_id
	JOIN
		orders o ON o.ord_id=oi.ord_id
	JOIN
		customers c ON o.cust_id=c.cust_id;



-- ===========================================================================================
-- USE OF VIEW
-- STORING BIG QUERIES INTO A VARIABLE OR VIEW
CREATE VIEW billing_info AS
SELECT 
	c.cust_name,
	o.ord_date,
	p.p_name,
	p.price,
	oi.quantity,
	(oi.quantity*p.price) AS total_price
FROM order_items oi
	JOIN
		products p ON oi.p_id=p.p_id
	JOIN
		orders o ON o.ord_id=oi.ord_id
	JOIN
		customers c ON o.cust_id=c.cust_id;	-- on the CMD you can check using \dv

-- THE MAIN IMPORTANT THING HERE IS THAT AFTER CREATING VIEW WE CAN DELETE OR REMOVE QUERIES
-- MEANS AFTER REMOVING ABOVE QUERY ALSO WE CAN USE ABOVE QUERY BY USING VIEW NAME THAT IS billing_info

-- GETTING ALL THE DATA USING VIEW
SELECT * FROM billing_info;

-- VIEW WITH GROUP BY
SELECT p_name, SUM(total_price)
FROM billing_info
GROUP BY p_name;

-- ===========================================================================================
-- HAVING CLAUSE
-- WHEN WE WANT ON GROUP BY CLAUSE THEN WE USE HAVING
SELECT p_name, SUM(total_price)
FROM billing_info
GROUP BY p_name
HAVING SUM(total_price)>500;

-- ROLLUP
-- GIVE THE TOTAL SUM OF total_price
SELECT p_name, SUM(total_price)
FROM billing_info
GROUP BY ROLLUP(p_name);   -- THE SUM WILL SHOW IN 1ST ROW IN ORDER TO SHOW IT DOWN USE FOLLOWING SYNTAX

-- IN ORDER TO SHOW THE TOTAL SUM OF total_price DOWN USE FOLLOWING SYNTAX
SELECT 
COALESCE(p_name, 'Total'), -- COALESCE() function will put total if there is any NULL value in the p_name column
SUM(total_price)
FROM billing_info
GROUP BY ROLLUP(p_name)
ORDER BY SUM(total_price);


-- ===========================================================================================
-- ===================
-- go to 2_basic.sql
-- ===================
-- ===========================================================================================


