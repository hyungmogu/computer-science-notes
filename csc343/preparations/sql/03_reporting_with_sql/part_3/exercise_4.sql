"""
===== Challenge Task 1 of 1 =====

We're in a movie database. There's a reviews table with the columns of id, movie_id, username, review and rating.

The movie 'Starman' has an id of 6. Movie ids are stored in the movie_id column. Calculate the average rating for 'Starman'.
Alias the average as average_rating.
"""

SELECT AVG(rating) AS "average_rating" FROM reviews WHERE movie_id = 6;