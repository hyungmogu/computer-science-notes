"""
===== Challenge Task 1 of 6 =====

There are two tables Fruit and Vegetable table. The Fruit table has a FruitID and
a Name column and the Vegetable table has a VegetableID and Name column.

Create a distinct result set of fruit and vegetable names.
"""


SELECT Name FROM Fruit
		UNION
SELECT Name FROM Vegetable;


"""
===== Challenge Task 2 of 6 =====

There are two tables Fruit and Vegetable table. The Fruit table has a FruitID and a Name column and the Vegetable table
has a VegetableID and Name column.

Create a list of all fruits and vegetables starting with the letters A through K . In other words all fruit and vegetables
that don't start with the letter L to Z.
"""

