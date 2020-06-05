"""
===== Challenge Task 1 of 2 =====

In the library database, how many books are in the genre of 'Science Fiction'?

Alias the result as scifi_book_count.

The books table has the columns id, title, author, genre and first_published.
"""


SELECT COUNT(*) AS "scifi_book_count" FROM books WHERE genre = 'Science Fiction';


"""
===== Challenge Task 2 of 2 =====

In the library database, how many books are by the author of 'J.K. Rowling'?

Alias the result as jk_book_count.

The books table has the columns id, title, author, genre and first_published.
"""

SELECT COUNT(*) AS "jk_book_count" FROM books WHERE author = 'J.K. Rowling';