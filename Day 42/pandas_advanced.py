import pandas as pd

df = pd.read_csv("employees.csv")
print(df)
print(df.head(3))
print(df[["Name", "Salary"]])
print(df[df["Salary"] > 35000])
print(df[(df["Age"] > 25) & (df["Salary"] > 40000)])
print(df.loc[1:2, ["Name", "Salary"]])
print(df.iloc[2:4, 0:2])
print(df.loc[4, "Salary"])
