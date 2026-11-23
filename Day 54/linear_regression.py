import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Step 3: Create Beam Deformation Dataset

data = {
    "Load": [100, 150, 200, 250, 300, 350, 400, 450, 500, 550],
    "Deformation": [2.5, 3.8, 5.2, 6.7, 8.1, 9.6, 11.0, 12.5, 14.1, 15.4],
}

df = pd.DataFrame(data)

print("Beam Deformation Dataset:")
print(df)
# Step 4: Prepare Input Features and Target

# Input feature
X = df[["Load"]]

# Target variable
y = df["Deformation"]

print("\nInput Features (X):")
print(X)

print("\nTarget Variable (y):")
print(y)
# Step 5: Train/Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\nTraining Records:", len(X_train))
print("Testing Records:", len(X_test))
# Step 6: Train Linear Regression Model

# Create the model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

print("\nLinear Regression Model Trained Successfully!")

# Predict deformation using test data
y_pred = model.predict(X_test)

print("\nPredicted Deformation (mm):")
print(y_pred)

print("\nActual Deformation (mm):")
print(y_test.values)
# Step 7: Coefficient, Intercept, and Residuals

# Get coefficient and intercept
coefficient = model.coef_[0]
intercept = model.intercept_

print("\nCoefficient:", round(coefficient, 4))
print("Intercept:", round(intercept, 4))

# Calculate residuals
residuals = y_test.values - y_pred

print("\nResiduals (mm):")
print(residuals)
# Step 8: Evaluate Model Performance

# Calculate Mean Absolute Error
mae = mean_absolute_error(y_test, y_pred)

# Calculate R2 Score
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation Results:")
print("Mean Absolute Error (MAE):", round(mae, 4))
print("R2 Score:", round(r2, 4))
