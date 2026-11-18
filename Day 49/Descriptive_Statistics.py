import pandas as pd

# Machine temperature dataset
data = {
    "Machine": [
        "M001",
        "M002",
        "M003",
        "M004",
        "M005",
        "M006",
        "M007",
        "M008",
        "M009",
        "M010",
    ],
    "Temperature": [45, 48, 50, 52, 55, 49, 51, 53, 47, 120],
}

df = pd.DataFrame(data)

print("Machine Temperature Dataset:")
print(df)
# Calculate Mean, Median and Mode

mean_temp = df["Temperature"].mean()
median_temp = df["Temperature"].median()
mode_temp = df["Temperature"].mode()[0]

print("\nDescriptive Statistics:")
print("Mean Temperature:", mean_temp)
print("Median Temperature:", median_temp)
print("Mode Temperature:", mode_temp)
# Calculate Range

max_temp = df["Temperature"].max()
min_temp = df["Temperature"].min()

range_temp = max_temp - min_temp

print("\nRange Calculation:")
print("Maximum Temperature:", max_temp)
print("Minimum Temperature:", min_temp)
print("Temperature Range:", range_temp)
# Calculate Variance

variance_temp = df["Temperature"].var()

print("\nVariance Calculation:")
print("Temperature Variance:", variance_temp)
# Calculate Standard Deviation

std_temp = df["Temperature"].std()

print("\nStandard Deviation Calculation:")
print("Temperature Standard Deviation:", std_temp)
# Detect Outliers Using IQR Method

Q1 = df["Temperature"].quantile(0.25)
Q3 = df["Temperature"].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df["Temperature"] < lower_bound) | (df["Temperature"] > upper_bound)]

print("\nOutlier Detection:")
print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower Bound:", lower_bound)
print("Upper Bound:", upper_bound)

print("\nDetected Outliers:")
print(outliers)
# Final Statistical Interpretation

print("\nFinal Analysis:")

print("Average Machine Temperature:", round(mean_temp, 2), "°C")
print("Median Machine Temperature:", median_temp, "°C")
print("Temperature Range:", range_temp, "°C")
print("Standard Deviation:", round(std_temp, 2), "°C")
print("Number of Outliers:", len(outliers))

if len(outliers) > 0:
    print("Some machines have unusual temperatures.")
    print("Further investigation is recommended.")
else:
    print("No statistical outliers detected.")
