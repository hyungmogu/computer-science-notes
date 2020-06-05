"""
===== Challenge Task 1 of 1 =====

In an ecommerce database there's an orders table with the columns id, product_id, user_id, address_id, ordered_on, status
and cost.

Count the total number of orders that were ordered yesterday and have the status of 'shipped'. Alias it to
ordered_yesterday_and_shipped.
"""


SELECT COUNT(*) AS "ordered_yesterday_and_shipped" FROM orders where status = 'shipped' AND ordered_on = Date("now", "-1 day");