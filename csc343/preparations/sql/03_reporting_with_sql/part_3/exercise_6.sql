"""
===== Challenge Task 1 of 1 =====

In an ecommerce database we have a products table with the columns id, name,
category, description, price and stock_count.

The price is in USD. Write a query that returns the product name and price in
Pounds Sterling (GBP). The current exchange rate is 1.4 USD to every 1 GBP.
Alias the calculated price to price_gbp. Round to two decimal places.
"""

SELECT name, ROUND(price / 1.4, 2) AS "price_gbp" FROM products;