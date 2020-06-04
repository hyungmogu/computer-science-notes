"""
===== Challenge Task 1 of 1 =====

In the library database there's a books table with the columns id, title, author,
genre and first_published.

Find the book with the longest title. Show the title and then the length. Alias
the result of the length calculation to be longest_length. Only retrieve the
longest book.
"""

SELECT title, LENGTH(title) AS "longest_length" FROM books ORDER BY LENGTH(title) DESC LIMIT 1;
