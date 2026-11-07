
-- ================================================
-- DAY 37: SQL SUBQUERIES AND CASE PRACTICE
-- ================================================
-- Topics Covered:
-- 1. Subquery Concept
-- 2. Scalar Subquery
-- 3. List Subquery
-- 4. CASE WHEN
-- 5. SQL Aliases
-- 6. Five Business Query Challenges
-- ================================================


-- ================================================
-- STEP 1: CREATE EMPLOYEES TABLE
-- ================================================

DROP TABLE IF EXISTS Employees;

CREATE TABLE Employees (
    Employee_ID INTEGER PRIMARY KEY,
    Name TEXT,
    Salary INTEGER
);


-- ================================================
-- STEP 2: INSERT SAMPLE DATA
-- ================================================

INSERT INTO Employees (Employee_ID, Name, Salary)
VALUES
(1, 'Arun', 30000),
(2, 'Priya', 50000),
(3, 'Ravi', 40000),
(4, 'Divya', 60000);


-- ================================================
-- STEP 3: DISPLAY ALL EMPLOYEE RECORDS
-- ================================================

SELECT * FROM Employees;


-- ================================================
-- TOPIC 1: SUBQUERY CONCEPT
-- Find employees earning above average salary
-- ================================================

SELECT Name, Salary
FROM Employees
WHERE Salary > (
    SELECT AVG(Salary)
    FROM Employees
);


-- ================================================
-- PRACTICAL QUESTION 1
-- Find employees earning below average salary
-- ================================================

SELECT Name, Salary
FROM Employees
WHERE Salary < (
    SELECT AVG(Salary)
    FROM Employees
);


-- ================================================
-- TOPIC 2: SCALAR SUBQUERY
-- Find employee earning the highest salary
-- ================================================

SELECT Name, Salary
FROM Employees
WHERE Salary = (
    SELECT MAX(Salary)
    FROM Employees
);


-- ================================================
-- TOPIC 3: LIST SUBQUERY
-- Find employees with salaries above 40000
-- using the IN operator
-- ================================================

SELECT Name, Salary
FROM Employees
WHERE Salary IN (
    SELECT Salary
    FROM Employees
    WHERE Salary > 40000
);


-- ================================================
-- PRACTICAL QUESTION 2
-- Find employees whose salaries are below 50000
-- using a list subquery
-- ================================================

SELECT Name, Salary
FROM Employees
WHERE Salary IN (
    SELECT Salary
    FROM Employees
    WHERE Salary < 50000
);


-- ================================================
-- TOPIC 4: CASE WHEN
-- Classify employees into High and Low Salary
-- ================================================

SELECT
    Name,
    Salary,
    CASE
        WHEN Salary >= 50000 THEN 'High Salary'
        ELSE 'Low Salary'
    END AS Salary_Category
FROM Employees;


-- ================================================
-- PRACTICAL QUESTION 3
-- Classify employees into three salary levels
-- ================================================

SELECT
    Name,
    Salary,
    CASE
        WHEN Salary >= 50000 THEN 'High Salary'
        WHEN Salary >= 40000 AND Salary < 50000
            THEN 'Medium Salary'
        ELSE 'Low Salary'
    END AS Salary_Level
FROM Employees;


-- ================================================
-- TOPIC 5: SQL ALIASES
-- Rename columns using AS
-- ================================================

SELECT
    Name AS Employee_Name,
    Salary AS Monthly_Salary
FROM Employees;


-- ================================================
-- PRACTICAL QUESTION 4
-- Employee salary report using column aliases
-- ================================================

SELECT
    Employee_ID AS ID,
    Name AS Employee_Name,
    Salary AS Monthly_Salary
FROM Employees;


-- ================================================
-- PRACTICAL QUESTION 5
-- FINAL BUSINESS QUERY
-- Find employees earning above average salary
-- and classify their salary levels
-- ================================================

SELECT
    Name AS Employee_Name,
    Salary AS Monthly_Salary,
    CASE
        WHEN Salary >= 55000 THEN 'Very High'
        ELSE 'High'
    END AS Salary_Level
FROM Employees
WHERE Salary > (
    SELECT AVG(Salary)
    FROM Employees
);


-- ================================================
-- DAY 37: ALL 5 PRACTICAL QUESTIONS COMPLETED
-- ================================================
