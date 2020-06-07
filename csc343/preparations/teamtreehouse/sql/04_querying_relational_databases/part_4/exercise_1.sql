"""
===== Challenge Task 1 of 5 =====

In a car database there is a Model table with columns, ModelID,
MakeID and ModelName and a Car table with columns, CarID, ModelID, VIN, ModelYear
and StickerPrice.

For all cars in the database, show Model Name, VIN and Sticker Price in one result set.
"""

SELECT ModelName, VIN, StickerPrice FROM Model AS md INNER JOIN Car as cr ON md.ModelID = cr.ModelID;


"""
===== Challenge Task 2 of 5 =====

In a car database there is a Make table with columns, MakeID and MakeName, a
Model table with columns, ModelID, MakeID and ModelName and a Car table with
columns, CarID, ModelID, VIN, ModelYear and StickerPrice.

For all cars in the database, show Make Name, Model Name, VIN and Sticker Price
from the Model and Car tables in one result set.
"""


SELECT MakeName, ModelName, VIN, StickerPrice FROM Model AS md
	INNER JOIN Make as mk ON md.MakeID = mk.MakeID
	INNER JOIN Car as cr ON md.ModelID = cr.ModelID;


"""
===== Challenge Task 3 of 5 =====

In a car database there is a Sale table with columns, SaleID, CarID, CustomerID,
LocationID, SalesRepID, SaleAmount and SaleDate. The database also has a SalesRep
table with columns, SalesRepID, FirstName, LastName, SSN, PhoneNumber,
StreetAddress, City, State and ZipCode.

Show the First and Last Name of each sales rep along with SaleAmount from both
the SalesRep and Sale tables in one result set.
"""

SELECT FirstName, LastName, SaleAmount FROM SalesRep AS sr
	INNER JOIN Sale as s ON sr.SalesRepID = s.SalesRepID;


"""
===== Challenge Task 4 of 5 =====

In a car database there is a Sale table with columns, SaleID, CarID, CustomerID,
LocationID, SalesRepID, SaleAmount and SaleDate. The database also has a SalesRep
table with columns, SalesRepID, FirstName, LastName, SSN, PhoneNumber,
StreetAddress, City, State and ZipCode.

Show the First and Last Name of each sales rep along with SaleAmount from both
the SalesRep and Sale tables in one result set.
"""

SELECT md.ModelName, cr.VIN FROM Model AS md
	LEFT OUTER JOIN Car as cr ON md.ModelID = cr.ModelID;


"""
===== Challenge Task 5 of 5 =====

In a car database there is a Sale table with columns, SaleID, CarID, CustomerID,
LocationID, SalesRepID, SaleAmount and SaleDate. The database also has a SalesRep
table with columns, SalesRepID, FirstName, LastName, SSN, PhoneNumber,
StreetAddress, City, State and ZipCode.

Show all SaleDate, SaleAmount, and SalesRep First and Last name from Sale and
SalesRep. Make sure that all Sales appear in results even if there is no
SalesRep associated to the sale.
"""

SELECT SaleDate, SaleAmount, FirstName, LastName FROM Sale AS s
    LEFT OUTER JOIN SalesRep AS sr ON s.SalesRepID = sr.SalesRepID;