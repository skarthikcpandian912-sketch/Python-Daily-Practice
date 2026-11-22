import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Step 3: Create Beam Deformation Dataset

data = {
    "Load": [100, 150, 200, 250, 300, 350, 400, 450, 500, 550],
    "Length": [500, 500, 600, 600, 700, 700, 800, 800, 900, 900],
    "Deformation": [2.5, 3.8, 6.2, 7.9, 10.5, 12.8, 15.6, 18.2, 21.5, 24.8],
}

df = pd.DataFrame(data)

print("Beam Deformation Dataset:")
print(df)

# Step 4: Prepare Features and Target

# Input features
X = df[["Load", "Length"]]

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

# Step 6: Create ML Pipeline

model = make_pipeline(StandardScaler(), LinearRegression())

print("\nML Pipeline Created Successfully!")

# Step 7: Train Model and Make Predictions

# Train the model
model.fit(X_train, y_train)

print("\nModel Trained Successfully!")

# Predict deformation using test data
y_pred = model.predict(X_test)

print("\nPredicted Deformation (mm):")
print(y_pred)

# Display actual deformation
print("\nActual Deformation (mm):")
print(y_test.values)

# Step 8: Evaluate Model Performance

mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation Results:")
print("Mean Absolute Error (MAE):", round(mae, 2))
print("R2 Score:", round(r2, 4))
