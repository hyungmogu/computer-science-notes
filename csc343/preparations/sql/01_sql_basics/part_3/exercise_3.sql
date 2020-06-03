"""
===== Challenge Task 1 of 2 =====

We're back in the sports team database. There's a results table with the columns
id, home_team, home_score, away_team, away_score and played_on .

Find all the matches in the results table where 'Hessle' was playing away as
the away team and their score was above 18 points.
"""

SELECT * FROM results WHERE away_team = 'Hessle' AND away_score > 18;


"""
===== Challenge Task 2 of 2 =====

Now we're in the e-commerce database. In the users table we have the columns id,
username, password, first_name and last_name.

Find all users with either the last name 'Hinkley' or 'Pettit'
"""

SELECT * FROM users WHERE last_name = 'Hinkley' OR last_name = 'Pettit';