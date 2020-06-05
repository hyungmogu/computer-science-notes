"""
===== Challenge Task 1 of 1 =====

We're in a movie database. There's a reviews table with the columns of id,
movie_id, username, review and rating.

The movie 'Starman' has the id of 6. Movie ids are found in the movie_id column
in the reviews table. Write a query that totals up all ratings for the movie
'Starman' in the reviews table. Alias it as starman_total_ratings.
"""


SELECT SUM(rating) AS "starman_total_ratings" FROM reviews WHERE movie_id = 6;