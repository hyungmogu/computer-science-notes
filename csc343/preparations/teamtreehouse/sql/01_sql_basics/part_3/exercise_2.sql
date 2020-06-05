"""
===== Challenge Task 1 of 3 =====

In our e-commerce database we have a users table with the columns id, username,
password, first_name and last_name.

Write a SQL query that retrieves the first and last names only where the username
is equal to 'wig_lady'.
"""

SELECT * FROM results WHERE home_score > 12;


"""
===== Challenge Task 2 of 3 =====

We're still using the sports team's database. In the results table we have the columns id, home_team, home_score,
away_team, away_score, played_on.

Find all results where the away team's score is lower than 10.
"""


SELECT * FROM results WHERE away_score < 10;



"""
===== Challenge Task 3 of 3 =====

We're back using the e-commerce database. I only have 10.99 left in my bank account. Write a query that will return all
products from the products table that I can afford.

The columns in the products are id, name, description and price.
"""

SELECT * FROM products WHERE price <= 10.99;

