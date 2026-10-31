-- Day 31: SQL Basics

-- Create Employees table
CREATE TABLE Employees (
    Employee_ID INT PRIMARY KEY,
    Name VARCHAR(50),
    Department VARCHAR(50)
);

-- Insert employee records
INSERT INTO Employees (Employee_ID, Name, Department)
VALUES
(101, 'Arun', 'IT'),
(102, 'Priya', 'HR'),
(103, 'Kumar', 'AI');

-- Display all employee records
SELECT * FROM Employees;

-- Display specific columns
SELECT Name, Department
FROM Employees;

-- Display only two records
SELECT *
FROM Employees
LIMIT 2;

-- Final practice challenge
SELECT Name
FROM Employees
LIMIT 2;