"""
===== Challenge Task 1 of 1 =====

In a movies database we have a movies table. It has the columns of id, title,
date_released and genre.

Write a query that returns the title first and the month and year it was released alias as month_year_released. Dates should
look like '04/1983' for April 1983.
"""


SELECT title, STRFTIME("%m/%Y", date_released) AS "month_year_released" FROM movies;