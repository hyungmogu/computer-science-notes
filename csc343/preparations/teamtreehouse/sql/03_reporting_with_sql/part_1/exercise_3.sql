"""
===== Challenge Task 1 of 2 =====

In a library database there's a books table. There's a title, author, genre and
first_published column.

The library database is connected to a website displaying 10 books at a time,
sorted by the title alphabetically.

Write a query to bring back the second page of results. Please retrieve all
columns of information.
"""

SELECT * FROM books ORDER BY title ASC LIMIT 10 OFFSET 10;


"""
===== Challenge Task 2 of 2 =====

In a library database there's a books table. There's a title, author, genre and
first_published column.

The library database is connected to a website displaying 10 books at a time,
sorted by the title alphabetically.

Write a query to bring back the second page of results. Please retrieve all
columns of information.
"""

SELECT * FROM phone_book ORDER BY last_name ASC, first_name ASC LIMIT 20 OFFSET 40;