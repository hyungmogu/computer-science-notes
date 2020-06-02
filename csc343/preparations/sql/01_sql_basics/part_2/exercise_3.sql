"""
===== Challenge Task 1 of 4 =====

We're back in our e-commerce database. There's a products table with the columns
id, name, description and price.

Can you retrieve both the name and description aliased as 'Product Name' and
'Product Description'.
"""


SELECT name AS 'Product Name', description AS 'Product Description' from products;


"""
===== Challenge Task 2 of 4 =====

In the users table we have columns of id, username, password, first_name and last_name.

Select the username and the first and last names and alias them as 'Username',
'First Name' and 'Last Name'.
"""

SELECT username AS 'Username', first_name AS 'First Name', last_name AS 'Last Name' from users;


"""
===== Challenge Task 3 of 4 =====

We're now back with the smartphone database. In the phone_book we have the columns
id, first_name, last_name and phone.

Alias the first and last names and phone as 'First Name', 'Last Name' and
'Phone Number'.
"""

SELECT first_name AS 'First Name', last_name AS 'Last Name', phone AS 'Phone Number' from phone_book;



"""
===== Challenge Task 4 of 4 =====

In this sports team database there's a results table with the columns of id,
home_team, home_score, away_team, away_score and played_on.

Alias 'Home Team', 'Home Score', 'Away Team', 'Away Score' and 'Date Played' to
the appropriate columns.
"""

SELECT home_team AS 'Home Team', home_score AS 'Home Score', away_team AS 'Away Team', away_score AS 'Away Score', played_on AS 'Date Played' FROM results;