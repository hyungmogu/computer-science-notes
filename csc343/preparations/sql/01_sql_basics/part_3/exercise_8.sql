"""
===== Challenge Task 1 of 2 =====

We're back on the smartphone, but our phone_book is a mess. There's a phone_book
table but there's missing information in a couple of the columns.

The phone_book has the following columns id, first_name, last_name and phone.

Find all contacts in the phone_book where the phone number is missing so we can go
and ask them for their number.
"""

SELECT * FROM phone_book WHERE phone IS NULL;

