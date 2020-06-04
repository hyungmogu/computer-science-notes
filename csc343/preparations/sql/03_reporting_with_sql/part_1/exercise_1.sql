"""
===== Challenge Task 1 of 3 =====

Imagine you're a developer on a smartphone with an embedded database. There's a
phone_book table with the fields, first_name, last_name and phone. Write the SQL
query to order first by last_name and then by first_name in alphabetical order.

Select all columns.
"""

SELECT * FROM phone_book ORDER BY last_name ASC, first_name ASC;
