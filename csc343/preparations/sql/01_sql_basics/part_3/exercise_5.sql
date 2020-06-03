"""
===== Challenge Task 1 of 2 =====

We have an e-commerce database. Inside the products table we have the columns of
id, name, description and price.

Without using the OR keyword, find all products with the price of 7.99, 9.99 or
11.99.
"""

SELECT * FROM products WHERE price IN (7.99, 9.99, 11.99);


"""
===== Challenge Task 2 of 2 =====

We have an e-commerce database. Inside the users table we have the columns of id,
username, password, first_name and last_name.

Without using the OR keyword, find all the users with the username of '2spooky4me'
or 'beard_man'.
"""

SELECT * FROM users WHERE username IN ('2spooky4me', 'beard_man');