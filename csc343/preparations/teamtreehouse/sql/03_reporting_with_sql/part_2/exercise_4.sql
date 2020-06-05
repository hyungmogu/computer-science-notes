"""
===== Challenge Task 1 of 1 =====

In an ecommerce database there's a customers table with id, username, first_name,
last_name, password, email and phone columns.

Create a report from the customers table that shows their first initial of their
first name and alias it as initial. Select their last name too.
"""


SELECT SUBSTR(first_name,1,1) AS "initial", last_name FROM customers;