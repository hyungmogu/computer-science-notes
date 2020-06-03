"""
===== Challenge Task 1 of 3 =====

In our e-commerce database we have a users table with the columns id, username,
password, first_name and last_name.

Write a SQL query that retrieves the first and last names only where the username
is equal to 'wig_lady'.
"""

SELECT first_name, last_name FROM users WHERE username = "wig_lady";


"""
===== Challenge Task 2 of 3 =====

In the products table we have the columns id, name, description and price.

Find all products that don't have the price of 9.99. Include all columns.
"""

SELECT * FROM products WHERE price != 9.99;


"""
===== Challenge Task 3 of 3 =====

In the products table we have the columns id, name, description and price.

Find all products that don't have the price of 9.99. Include all columns.
"""


SELECT username FROM users WHERE last_name = 'Chalkley';