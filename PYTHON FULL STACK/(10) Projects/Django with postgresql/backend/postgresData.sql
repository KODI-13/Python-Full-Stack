SELECT * FROM zomato_customers;

SELECT * FROM zomato_orders;

SELECT * FROM zomato_products;

SELECT * FROM zomato_orderitem;


SELECT zc.cust_name, zo.ord_date, zo.id AS ord_id, quantity
FROM zomato_orderitem zoi
JOIN zomato_orders zo ON zoi.order_id = zo.id
JOIN zomato_products zp ON zoi.product_id = zp.id
JOIN zomato_customers zc ON zc.id = zo.customer_id;