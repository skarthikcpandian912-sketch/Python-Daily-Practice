import pandas as pd

ages = pd.Series([25, 28, 30])

print("Employee Ages:")
print(ages)
# Topic 2: Pandas DataFrame

data = {
    "Name": ["Arun", "Priya", "Kumar"],
    "Age": [25, 28, 30],
    "Salary": [30000, 40000, 50000],
}

df = pd.DataFrame(data)

print("Employee DataFrame:")
print(df)
# Topic 3: Pandas Columns and Index

print("Column Names:")
print(df.columns)

print("Row Index:")
print(df.index)

print("Name Column:")
print(df["Name"])

print("First Employee Name:")
print(df.loc[0, "Name"])
# Topic 4: Pandas head() and tail()

employees = {
    "Name": ["Arun", "Priya", "Kumar", "Divya", "Ravi", "Meena"],
    "Age": [25, 28, 30, 24, 32, 27],
}

employee_df = pd.DataFrame(employees)

print("First 3 Employees:")
print(employee_df.head(3))

print("Last 2 Employees:")
print(employee_df.tail(2))
# Topic 5: Pandas info() and describe()

employee_data = {
    "Name": ["Arun", "Priya", "Kumar", "Divya", "Ravi"],
    "Age": [25, 28, 30, 24, 32],
    "Salary": [30000, 40000, 50000, 35000, 45000],
}

employee_df = pd.DataFrame(employee_data)

print("DataFrame Information:")
employee_df.info()

print("\nStatistical Summary:")
print(employee_df.describe())
marks = pd.Series([75, 80, 85, 90, 95])
print("Marks:")
print(marks)
students = {
    "Name": ["Arun", "Priya", "Kumar", "Divya", "Ravi"],
    "Age": [20, 21, 22, 20, 23],
    "Marks": [75, 80, 85, 90, 95],
}
df = pd.DataFrame(students)
print("Student Information:")
print(df)
print("Name Column:")
print(df["Name"])
print("Column Names:")
print(df.columns)
print("Row Index:")
print(df.index)
employees = {
    "Name": ["Arun", "Priya", "Kumar", "Divya", "Ravi", "Meena", "Karthik", "Anu"],
    "Age": [25, 28, 30, 24, 32, 27, 29, 26],
    "Salary": [30000, 40000, 50000, 35000, 45000, 38000, 42000, 36000],
}
employees_df = pd.DataFrame(employees)
print("first 3 employees:")
print(employees_df.head(3))
print(employees_df.head(5))
print(employees_df.tail(2))
print(employees_df.tail(3))
employee_data = {
    "Name": ["Arun", "Priya", "Kumar", "Divya", "Ravi"],
    "Age": [25, 28, 30, 24, 32],
    "Salary": [30000, 40000, 50000, 35000, 45000],
}
employees_df = pd.DataFrame(employee_data)
print("DataFrame Information:")
employees_df.info()
print("\n Statistical Summary:")
print(employees_df.describe())
print("Average Salary:", employees_df["Salary"].mean())
print("Maximum Salary:", employees_df["Salary"].max())
print("Minimum Salary:", employees_df["Salary"].min())
