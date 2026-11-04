-- STEP 1: CREATE SALES TABLE

DROP TABLE IF EXISTS Sales;

CREATE TABLE Sales (
    Sale_ID INTEGER PRIMARY KEY,
    Product TEXT,
    Amount INTEGER
);


-- STEP 2: INSERT SALES DATA

INSERT INTO Sales (Sale_ID, Product, Amount)
VALUES
(1, 'Laptop', 50000),
(2, 'Mouse', 500),
(3, 'Keyboard', 1500),
(4, 'Monitor', 12000),
(5, 'Headphones', 2500),
(6, 'Laptop', 55000),
(7, 'Mouse', 700);


-- STEP 3: DISPLAY ALL RECORDS

SELECT * FROM Sales;


-- ============================================
-- QUESTION 1
-- Count total sales records for each product
-- ============================================

SELECT Product, COUNT(*) AS Total_Orders
FROM Sales
GROUP BY Product;


-- ============================================
-- QUESTION 2
-- Calculate average sales for each product
-- ============================================

SELECT Product, AVG(Amount) AS Average_Sales
FROM Sales
GROUP BY Product;


-- ============================================
-- QUESTION 3
-- Display products having more than one sale
-- ============================================

SELECT Product, COUNT(*) AS Total_Orders
FROM Sales
GROUP BY Product
HAVING COUNT(*) > 1;


-- ============================================
-- QUESTION 4
-- Display products with average sales > 5000
-- ============================================

SELECT Product, AVG(Amount) AS Average_Sales
FROM Sales
GROUP BY Product
HAVING AVG(Amount) > 5000;


-- ============================================
-- QUESTION 5
-- Find minimum and maximum sales per product
-- ============================================

SELECT
    Product,
    MIN(Amount) AS Minimum_Sales,
    MAX(Amount) AS Maximum_Sales
FROM Sales
GROUP BY Product;


-- ============================================
-- QUESTION 6
-- Calculate total sales for each product
-- considering only records with Amount > 1000
-- ============================================

SELECT Product, SUM(Amount) AS Total_Sales
FROM Sales
WHERE Amount > 1000
GROUP BY Product;


-- ============================================
-- QUESTION 7
-- Display products with total sales > 2000
-- Sort from highest to lowest
-- ============================================

SELECT Product, SUM(Amount) AS Total_Sales
FROM Sales
GROUP BY Product
HAVING SUM(Amount) > 2000
ORDER BY Total_Sales DESC;


-- ============================================
-- QUESTION 8
-- FINAL GROUP BY CHALLENGE
-- 1. Filter Amount >= 1000
-- 2. Group records by Product
-- 3. Calculate total sales
-- 4. Display totals > 10000
-- 5. Sort in descending order
-- ============================================

SELECT Product, SUM(Amount) AS Total_Sales
FROM Sales
WHERE Amount >= 1000
GROUP BY Product
HAVING SUM(Amount) > 10000
ORDER BY Total_Sales DESC;