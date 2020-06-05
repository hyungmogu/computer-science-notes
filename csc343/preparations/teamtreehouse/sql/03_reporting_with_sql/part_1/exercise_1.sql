"""
===== Challenge Task 1 of 3 =====

Imagine you're a developer on a smartphone with an embedded database. There's a
phone_book table with the fields, first_name, last_name and phone. Write the SQL
query to order first by last_name and then by first_name in alphabetical order.

Select all columns.
"""

SELECT * FROM phone_book ORDER BY last_name ASC, first_name ASC;


"""
===== Challenge Task 2 of 3 =====

In a library database there's a books table. There's a title, author, genre and
first_published column.

Order the books by the most recently published books at the top. Select all columns.
"""

SELECT * FROM books ORDER BY first_published DESC;


"""
===== Challenge Task 3 of 3 =====

We're still using the library database there's a books table. There's a title,
author, genre and first_published column.

Order all books by Genre and then by Title. Select all columns.
"""

SELECT * FROM books ORDER BY genre ASC, title ASC;