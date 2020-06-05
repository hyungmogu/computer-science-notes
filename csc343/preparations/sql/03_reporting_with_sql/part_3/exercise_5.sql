"""
===== Challenge Task 1 of 1 =====

We're in a movie database. There's a reviews table with the columns of id,
movie_id, username, review and rating.

The movie 'Starman' has an id of 6. Movie ids are stored in the movie_id column.
Calculate the minimum and maximum ratings for 'Starman'. Alias them as
star_min and star_max.
"""

SELECT MIN(rating) AS "star_min", MAX(rating) AS "star_max" FROM reviews WHERE movie_id = 6;