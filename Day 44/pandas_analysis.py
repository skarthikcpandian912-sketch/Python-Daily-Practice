import pandas as pd

employees = {
    "Name": ["Arun", "Priya", "Kumar", "Divya", "Rahul", "Meena"],
    "Department": ["IT", "HR", "Finance", "IT", "HR", "Finance"],
    "Salary": [30000, 50000, 40000, 35000, 60000, 45000],
}

df = pd.DataFrame(employees)
print(df)
print(df.sort_values(by="Salary", ascending=False))
print(df.groupby("Department")["Salary"].sum())
print(df.groupby("Department")["Salary"].agg(["max", "min", "mean"]))
print(df["Department"].value_counts())
df["Salary_Category"] = df["Salary"].apply(lambda x: "High" if x >= 50000 else "Normal")
print(df)
