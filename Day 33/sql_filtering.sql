-- Day 33: SQL Filtering Practice
-- Topics: WHERE, Comparison Operators, AND, OR, NOT, IN, BETWEEN, LIKE

-- Create Employees table
CREATE TABLE IF NOT EXISTS Employees (
    Employees_ID INTEGER PRIMARY KEY,
    Name TEXT,
    Department TEXT
);

-- Insert sample employee data
INSERT INTO Employees (Employees_ID, Name, Department)
VALUES
(101, 'Arun', 'IT'),
(102, 'Priya', 'HR'),
(103, 'Kumar', 'AI'),
(104, 'Ravi', 'IT'),
(105, 'Meena', 'AI');


-- Query 1: Employees in AI department
SELECT *
FROM Employees
WHERE Department = 'AI';


-- Query 2: Employee ID greater than or equal to 103
SELECT *
FROM Employees
WHERE Employees_ID >= 103;


-- Query 3: Employees not in IT department
SELECT *
FROM Employees
WHERE Department != 'IT';


-- Query 4: AND operator
SELECT *
FROM Employees
WHERE Department = 'IT'
AND Employees_ID > 101;


-- Query 5: OR operator
SELECT *
FROM Employees
WHERE Department = 'IT'
OR Employees_ID = 103;


-- Query 6: NOT operator
SELECT *
FROM Employees
WHERE NOT Employees_ID > 103;


-- Query 7: IN operator
SELECT *
FROM Employees
WHERE Employees_ID IN (102, 103, 105);


-- Query 8: BETWEEN operator
SELECT *
FROM Employees
WHERE Employees_ID BETWEEN 102 AND 104;


-- Query 9: LIKE operator
SELECT *
FROM Employees
WHERE Name LIKE 'M%';


-- Query 10: Combined IN, BETWEEN and AND
SELECT *
FROM Employees
WHERE Department IN ('IT', 'AI')
AND Employees_ID BETWEEN 103 AND 105;