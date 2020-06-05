"""
===== Challenge Task 1 of 1 =====

In an ecommerce database there's an orders table with the columns id, product_id,
user_id, address_id, ordered_on, status and cost.

Count the total number of orders that were ordered today and have the status of
'shipped'. Alias it to shipped_today.
"""


SELECT COUNT(*) AS "shipped_today" FROM orders WHERE status = "shipped" AND ordered_on = DATE("now");