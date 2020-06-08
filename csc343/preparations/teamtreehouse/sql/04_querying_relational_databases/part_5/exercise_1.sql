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


SELECT Name FROM Fruit
	WHERE Name < "L"
		UNION
SELECT Name FROM Vegetable
	WHERE Name < "L";


"""
===== Challenge Task 3 of 6 =====

There are two tables Fruit and Vegetable table. The Fruit table has a FruitID and a Name column and the Vegetable table
has a VegetableID and Name column.

Create a list of all fruits and vegetables starting with the letters A through K . In other words all fruit and vegetables
that don't start with the letter L to Z.
"""

SELECT Name FROM Fruit
		UNION ALL
SELECT Name FROM Vegetable
	ORDER BY Name;


"""
===== Challenge Task 4 of 6 =====

There are two tables Fruit and Vegetable table. The Fruit table has a FruitID
and a Name column and the Vegetable table has a VegetableID and Name column.

Create an alphabetical list of produce that is considered both a fruit and a
vegetable.
"""

SELECT Name FROM Fruit
		INTERSECT
SELECT Name FROM Vegetable
	ORDER BY Name;



"""
===== Challenge Task 5 of 6 =====

There are two tables Fruit and Vegetable table. The Fruit table has a FruitID and
a Name column and the Vegetable table has a VegetableID and Name column.

Create an alphabetical list of fruits that are NOT considered a vegetable.
"""

SELECT Name FROM Fruit
		EXCEPT
SELECT Name FROM Vegetable
	ORDER BY Name;


"""
===== Challenge Task 6 of 6 =====

There are two tables Fruit and Vegetable table. The Fruit table has a FruitID
and a Name column and the Vegetable table has a VegetableID and Name column.

Create an alphabetical list of vegetables that are NOT considered a fruit.
"""


SELECT Name FROM Vegetable
		EXCEPT
SELECT Name FROM Fruit
	ORDER BY Name;