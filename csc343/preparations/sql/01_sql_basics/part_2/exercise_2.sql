"""
===== Challenge Task 1 of 5 =====

Here are the columns in a users table in an e-commerce site: id, username,
password, first_name, last_name.

Run a SQL query to get the two columns you'd need to generate the full names of
each customer.
"""

SELECT first_name, last_name from users;


"""
===== Challenge Task 2 of 5 =====

We're still in the e-commerce database. This time, from the products table, get
the name of every product.
"""

SELECT name from products;


"""
===== Challenge Task 3 of 5 =====

In the e-commerce database there's a customer_addresses table with the following
columns: id, nickname, street, city, state, zip, user_id.

Select all the columns that are to do with the address. For example, all columns
except id, nickname and user_id.
"""

SELECT street, city, state, zip FROM customer_addresses;


"""
===== Challenge Task 4 of 5 =====

We're using a database on a smartphone again. We have a phone_book table. In
here there's an id, first_name, last_name and phone.

As the user types the phone number in we want to show possible autocomplete values.
Bring back only the phone numbers of each contact only. Our smartphone can work out
which of the results to show.
"""

SELECT phone FROM phone_book;



"""
===== Challenge Task 5 of 5 =====

We're using a database on a smartphone again. We have a phone_book table. In
here there's an id, first_name, last_name and phone.

As the user types the phone number in we want to show possible autocomplete values.
Bring back only the phone numbers of each contact only. Our smartphone can work out
which of the results to show.
"""

SELECT first_name, last_name FROM phone_book;