"""
===== Challenge Task 1 of 2 =====

In a library database there's a books table. There's an id, title, author, genre
and first_published column.

Write a query that will return only the title and author. Bring back the title
in lowercase and the author in uppercase. Alias them as lowercase_title and
uppercase_author respectively.
"""

SELECT LOWER(title) AS "lowercase_title", UPPER(author) AS "uppercase_author" FROM books;


"""
===== Challenge Task 2 of 2 =====

In the library database there's a patrons table with the columns id, first_name, last_name, address, email, library_id,
and zip_code.

The library is generating new library cards that will display the full name and
their library ID. The full name needs to have the last name in all caps. Create
a report with two columns of results, one is an alias of full_name the second
being the library_id.
"""

SELECT first_name || " " || UPPER(last_name) AS "full_name", library_id FROM patrons;