"""
===== Challenge Task 1 of 2 =====

We're using the library database again. There's a books table. There's a title,
author, genre and first_published column.

Write a query to obtain the first 5 books in the Fantasy genre ordered by the year
released. Oldest first. Select all columns.
"""

SELECT * FROM books WHERE genre = 'Fantasy' ORDER BY first_published ASC LIMIT 5;


"""
===== Challenge Task 2 of 2 =====

We're still using the library database with the books table. There's a title,
author, genre and first_published column.

Find the earliest Science Fiction book in our library. Only one result should be
returned. All columns should be selected.
"""

SELECT * FROM books WHERE genre = 'Science Fiction' ORDER BY first_published ASC LIMIT 1;
