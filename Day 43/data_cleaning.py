import pandas as pd

employees = {
    "Name": ["Arun", "Priya", "Kumar", "Divya", "Rahul"],
    "Age": [25, None, 30, 24, None],
    "Salary": [30000, 40000, None, 35000, 50000],
}

df = pd.DataFrame(employees)
print(df)
print(df.isna())
print(df.isna().sum())
df["Age"] = df["Age"].fillna(26)
df["Salary"] = df["Salary"].fillna(35000)
print(df)
import pandas as pd

employees = {
    "Name": ["Arun", "Priya", "Kumar", "Arun", "Divya", "Priya"],
    "Age": [25, 27, 30, 25, 24, 27],
    "Salary": [30000, 40000, 50000, 30000, 35000, 40000],
}

df = pd.DataFrame(employees)
print(df)
print(df.duplicated())
print(df.duplicated().sum())
df = df.drop_duplicates()
print(df)
import pandas as pd

employees = {
    "Name": ["Arun", "Priya", "Kumar", "Divya"],
    "Age": ["25", "27", "30", "24"],
    "Salary": [30000, 40000, 50000, 35000],
}

df = pd.DataFrame(employees)
print(df)
print(df.dtypes)
df["Age"] = pd.to_numeric(df["Age"])
print(df.dtypes)
df = df.rename(columns={"Name": "Employee_Name"})
df = df.rename(columns={"Salary": "Monthly_Salary"})
print(df)
