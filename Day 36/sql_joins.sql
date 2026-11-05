
-- ==========================================
-- DAY 36: SQL JOINS PRACTICE
-- ==========================================
-- Topics:
-- 1. Table Relationships
-- 2. INNER JOIN
-- 3. LEFT JOIN
-- 4. RIGHT JOIN
-- 5. Join Keys
-- ==========================================

-- STEP 1: CREATE TABLES

DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Customers;

CREATE TABLE Customers (
    Customer_ID INTEGER PRIMARY KEY,
    Name TEXT
);

CREATE TABLE Orders (
    Order_ID INTEGER PRIMARY KEY,
    Customer_ID INTEGER,
    FOREIGN KEY (Customer_ID)
        REFERENCES Customers(Customer_ID)
);

-- STEP 2: INSERT DATA

INSERT INTO Customers (Customer_ID, Name)
VALUES
(1, 'Arun'),
(2, 'Priya'),
(3, 'Ravi');

INSERT INTO Orders (Order_ID, Customer_ID)
VALUES
(101, 1),
(102, 2),
(103, 1);

-- STEP 3: DISPLAY TABLES

SELECT * FROM Customers;
SELECT * FROM Orders;


-- ==========================================
-- PRACTICE 1: INNER JOIN
-- Display customer names and order IDs
-- ==========================================

SELECT Customers.Name, Orders.Order_ID
FROM Customers
INNER JOIN Orders
ON Customers.Customer_ID = Orders.Customer_ID;


-- ==========================================
-- PRACTICE 2: INNER JOIN
-- Display customer ID, name, and order ID
-- ==========================================

SELECT
    Customers.Customer_ID,
    Customers.Name,
    Orders.Order_ID
FROM Customers
INNER JOIN Orders
ON Customers.Customer_ID = Orders.Customer_ID;


-- ==========================================
-- PRACTICE 3: LEFT JOIN
-- Display all customers including those
-- without orders
-- ==========================================

SELECT Customers.Name, Orders.Order_ID
FROM Customers
LEFT JOIN Orders
ON Customers.Customer_ID = Orders.Customer_ID;


-- ==========================================
-- PRACTICE 4: LEFT JOIN
-- Display all customers with their IDs
-- ==========================================

SELECT
    Customers.Customer_ID,
    Customers.Name,
    Orders.Order_ID
FROM Customers
LEFT JOIN Orders
ON Customers.Customer_ID = Orders.Customer_ID;


-- ==========================================
-- PRACTICE 5: RIGHT JOIN
-- Display all customers including Ravi
-- ==========================================

SELECT Customers.Name, Orders.Order_ID
FROM Orders
RIGHT JOIN Customers
ON Orders.Customer_ID = Customers.Customer_ID;


-- ==========================================
-- PRACTICE 6: JOIN KEYS
-- Connect tables using Customer_ID
-- ==========================================

SELECT
    Customers.Name,
    Orders.Order_ID,
    Customers.Customer_ID
FROM Customers
INNER JOIN Orders
ON Customers.Customer_ID = Orders.Customer_ID;


-- ==========================================
-- DAY 36 SQL PRACTICE COMPLETED
-- ==========================================
