import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score

# Actual machine conditions
y_actual = [0, 0, 1, 1, 0, 1, 0, 1, 0, 1]

# Model A predictions
model_a = [0, 0, 1, 0, 0, 1, 0, 0, 0, 1]

# Model B predictions
model_b = [0, 1, 1, 1, 0, 1, 0, 1, 1, 1]
# Calculate Accuracy
accuracy_a = accuracy_score(y_actual, model_a)
accuracy_b = accuracy_score(y_actual, model_b)

print("Model A Accuracy:", accuracy_a * 100, "%")
print("Model B Accuracy:", accuracy_b * 100, "%")
# Calculate Precision
precision_a = precision_score(y_actual, model_a)
precision_b = precision_score(y_actual, model_b)

print("Model A Precision:", round(precision_a * 100, 2), "%")
print("Model B Precision:", round(precision_b * 100, 2), "%")
# Calculate Recall
recall_a = recall_score(y_actual, model_a)
recall_b = recall_score(y_actual, model_b)

print("Model A Recall:", round(recall_a * 100, 2), "%")
print("Model B Recall:", round(recall_b * 100, 2), "%")
# Calculate F1-score
f1_a = f1_score(y_actual, model_a)
f1_b = f1_score(y_actual, model_b)

print("Model A F1-score:", round(f1_a * 100, 2), "%")
print("Model B F1-score:", round(f1_b * 100, 2), "%")
# Compare model performance
comparison = pd.DataFrame(
    {
        "Metric": ["Accuracy", "Precision", "Recall", "F1-score"],
        "Model A": [accuracy_a, precision_a, recall_a, f1_a],
        "Model B": [accuracy_b, precision_b, recall_b, f1_b],
    }
)

# Convert metrics into percentages
comparison["Model A"] = (comparison["Model A"] * 100).round(2)
comparison["Model B"] = (comparison["Model B"] * 100).round(2)

print("\nModel Performance Comparison (%)")
print(comparison.to_string(index=False))
# Class Imbalance Example
y_imbalanced = [0] * 95 + [1] * 5

# Model predicts all machines as normal
y_pred_imbalanced = [0] * 100

# Calculate classification metrics
accuracy = accuracy_score(y_imbalanced, y_pred_imbalanced)

precision = precision_score(y_imbalanced, y_pred_imbalanced, zero_division=0)

recall = recall_score(y_imbalanced, y_pred_imbalanced)

f1 = f1_score(y_imbalanced, y_pred_imbalanced)

print("\nClass Imbalance Results")
print("Accuracy:", accuracy * 100, "%")
print("Precision:", precision * 100, "%")
print("Recall:", recall * 100, "%")
print("F1-score:", f1 * 100, "%")
