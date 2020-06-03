"""
===== Challenge Task 1 of 2 =====

We have an e-commerce database. Inside the products table we have the columns of
id, name, description and price.

Without using the OR keyword, find all products with the price of 7.99, 9.99 or
11.99.
"""

SELECT * FROM products WHERE price IN (7.99, 9.99, 11.99);