-- Topics Covered:
-- 1. ORDER BY
-- 2. DISTINCT
-- 3. COUNT()
-- 4. SUM()
-- 5. AVG()
-- 6. MIN() and MAX()

-- ==========================================
-- STEP 1: CREATE SALES TABLE
-- ==========================================

DROP TABLE IF EXISTS Sales;

CREATE TABLE Sales (
    Sale_ID INTEGER PRIMARY KEY,
    Product TEXT,
    Amount INTEGER
);

-- ==========================================
-- STEP 2: INSERT SAMPLE DATA
-- ==========================================

INSERT INTO Sales (Sale_ID, Product, Amount)
VALUES
(1, 'Laptop', 50000),
(2, 'Mouse', 500),
(3, 'Keyboard', 1500),
(4, 'Monitor', 12000),
(5, 'Headphones', 2500),
(6, 'Laptop', 55000),
(7, 'Mouse', 700);

-- View all records
SELECT * FROM Sales;


-- ==========================================
-- QUERY 1: ORDER BY
-- Sort sales from lowest to highest
-- ==========================================

SELECT *
FROM Sales
ORDER BY Amount ASC;


-- ==========================================
-- QUERY 2: DISTINCT
-- Display unique product names
-- ==========================================

SELECT DISTINCT Product
FROM Sales;


-- ==========================================
-- QUERY 3: COUNT()
-- Count unique products
-- ==========================================

SELECT COUNT(DISTINCT Product)
AS Total_Unique_Products
FROM Sales;


-- ==========================================
-- QUERY 4: SUM()
-- Calculate total Laptop sales
-- ==========================================

SELECT SUM(Amount)
AS Laptop_Total_Sales
FROM Sales
WHERE Product = 'Laptop';


-- ==========================================
-- QUERY 5: AVG()
-- Calculate average Laptop sales
-- ==========================================

SELECT AVG(Amount)
AS Laptop_Average_Sales
FROM Sales
WHERE Product = 'Laptop';


-- ==========================================
-- QUERY 6: MIN() AND MAX()
-- Find minimum and maximum Laptop sales
-- ==========================================

SELECT
    MIN(Amount) AS Minimum_Laptop_Sales,
    MAX(Amount) AS Maximum_Laptop_Sales
FROM Sales
WHERE Product = 'Laptop';

-- ==========================================
-- END OF DAY 34 SQL PRACTICE
-- ==========================================