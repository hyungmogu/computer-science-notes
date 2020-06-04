"""
===== Challenge Task 1 of 3 =====

We have an eCommerce database and it has a products table. It has the columns id,
name, description and price.

Add a new product to the products table. Use any valid values you want. All columns
are required. The id column is auto incrementing.
"""


INSERT INTO products VALUES (0, 'Ice cream', 'deliciousness', 9.99);


"""
===== Challenge Task 2 of 3 =====

The same eCommerce database has a users table. It has the columns id, username,
password, first_name, and last_name.

Add a new user to the users table. Use any valid values you want. All columns are
required. The id column is auto incrementing.

(Don't enter a real password you'd really use!)
"""

INSERT INTO users (id, username, first_name, last_name) VALUES (0, 'helloworld12', 'Moe', 'Gu');



"""
===== Challenge Task 3 of 3 =====

Now we're using a database from a smartphone. It has a phone_book table. It has
the columns id, first_name, last_name and phone.

Add a new contact to the phone_book table. Use any valid values you want. All columns
are required. The id column is auto incrementing.
"""

INSERT INTO phone_book VALUES (0, 'Moe', 'Gu', '111-222-3333');
