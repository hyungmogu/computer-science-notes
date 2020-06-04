"""
===== Challenge Task 1 of 2 =====

In the library database there's a patrons table listing all the users of the
library. The columns are id, first_name, last_name, address, email, library_id
and zip_code.

Generate a list of strings that are in the following format: Andrew Chalkley
<andrew@teamtreehouse.com>. Concatenate the first name, last name and email
address for all users.

Alias it to to_field. This will be used in the 'To' field in email marketing.
"""


SELECT first_name || ' ' || last_name || ' <' || email || '>' AS "to_field"  FROM patrons;


"""
===== Challenge Task 2 of 2 =====

In an ecommerce database there's a addresses table. There is an id, nickname, street, city, state, zip, country and
user_id columns.

Concatenate the street, city, state, zip and country in the following format. Street, City, State Zip. Country e.g. 34
NE 12 st, Portland, OR 97129. USA

Alias the concatenated string as address
"""

SELECT street || ', ' || city || ', ' || state || ' ' || zip || '. ' || country AS address FROM addresses;