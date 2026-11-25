import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Create machine dataset
data = {
    "Temperature": [30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105],
    "Vibration": [
        1.2,
        1.5,
        1.8,
        2.1,
        2.5,
        2.8,
        3.2,
        3.5,
        4.8,
        5.2,
        5.8,
        6.2,
        6.8,
        7.2,
        7.8,
        8.5,
    ],
    "Failure": [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
}

df = pd.DataFrame(data)

print(df)
# Define input features
X = df[["Temperature", "Vibration"]]

# Define target variable
y = df["Failure"]
# Split dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

print("Training records:", len(X_train))
print("Testing records:", len(X_test))
# Create Logistic Regression model
model = LogisticRegression()

# Train the model
model.fit(X_train, y_train)

print("Model trained successfully!")
# Predict failure classes
y_pred = model.predict(X_test)

# Predict class probabilities
y_prob = model.predict_proba(X_test)

print("\nActual values:")
print(y_test.values)

print("\nPredicted values:")
print(y_pred)

print("\nPredicted probabilities:")
print(y_prob)
# Evaluate model accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", accuracy)
print(f"Model Accuracy Percentage: {accuracy * 100:.2f}%")
# Get new machine input
temperature = float(input("\nEnter machine temperature (°C): "))
vibration = float(input("Enter machine vibration (mm/s): "))

# Create new machine data
new_machine = pd.DataFrame({"Temperature": [temperature], "Vibration": [vibration]})

# Predict failure
prediction = model.predict(new_machine)

# Predict probability
probability = model.predict_proba(new_machine)

# Display results
if prediction[0] == 1:
    print("\nPrediction: Machine Failure")
else:
    print("\nPrediction: No Machine Failure")

print(f"No Failure Probability: {probability[0][0] * 100:.2f}%")
print(f"Failure Probability: {probability[0][1] * 100:.2f}%")
