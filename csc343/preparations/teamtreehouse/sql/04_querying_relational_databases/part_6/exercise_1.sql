"""
===== Challenge Task 1 of 6 =====

In a car database there is a Model table with columns, ModelID, MakeID and
ModelName and a Car table with columns, CarID, ModelID, VIN, ModelYear and
StickerPrice.

Use a subquery along with IN to list all the Model Names with a Sticker Price
greater than $30000
"""

SELECT ModelName FROM Model
    WHERE ModelID IN (
        SELECT ModelID FROM Car WHERE StickerPrice > 30000
    );

"""
===== Challenge Task 2 of 4 =====

In a car database there is a Sale table with columns, SaleID, CarID, CustomerID,
LocationID, SalesRepID, SaleAmount and SaleDate and a Car table with columns,
CarID, ModelID, VIN, ModelYear and StickerPrice.

Use a subquery along with IN to list all sales of cars with Sticker Price greater
than $30000. Include all columns.
"""


SELECT * FROM Sale
    WHERE CarID IN (
        SELECT CarID FROM Car WHERE StickerPrice > 30000
    );


"""
===== Challenge Task 3 of 4 =====

In a car database there is a Sale table with columns, SaleID, CarID, CustomerID,
LocationID, SalesRepID, SaleAmount and SaleDate and a Customer table with columns,
CustomerID, FirstName, LastName, Gender and SSN.

Use a subquery along with IN to list all sales to female customers. (Gender = 'F')
Select all columns.
"""

SELECT * FROM Sale
    WHERE CustomerID IN (
        SELECT CustomerID FROM Customer WHERE Gender = 'F'
    );


"""
===== Challenge Task 4 of 4 =====

In a car database there is a Sale table with columns, SaleID, CarID, CustomerID,
LocationID, SalesRepID, SaleAmount and SaleDate and a Customer table with columns,
CustomerID, FirstName, LastName, Gender and SSN.

Use a subquery as a derived table to show all sales to female ('F') customers.
Select all columns from the Sale table only.
"""


SELECT * FROM Sale AS s
		INNER JOIN (
        SELECT CustomerID FROM Customer WHERE Gender = 'F'
    ) AS c ON s.CustomerID = c.CustomerID;
