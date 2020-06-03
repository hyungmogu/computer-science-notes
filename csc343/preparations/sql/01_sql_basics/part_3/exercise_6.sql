"""
===== Challenge Task 1 of 2 =====

In the e-commerce database we have the products table with the columns id, name,
description and price.

Find all the products in the database with the price including and between 10.99
and 12.99.
"""


SELECT * FROM products WHERE price BETWEEN 10.99 and 12.99;


"""
===== Challenge Task 2 of 2 =====

We're back in our sports team database with the results table. The columns are id,
home_team, home_score, away_team, away_score and played_on.

There are 30 days in September. Find all the games played in the results table
in September 2015.
"""

SELECT * FROM results WHERE played_on BETWEEN '2015-09-01' AND '2015-09-30';