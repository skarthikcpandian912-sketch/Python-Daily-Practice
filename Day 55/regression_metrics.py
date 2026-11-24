import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Actual beam deformation values
actual = [10, 20, 30, 40, 50]

# Model A predictions
model_a = [12, 22, 32, 42, 52]

# Model B predictions
model_b = [10, 20, 30, 40, 60]
# Calculate metrics for Model A
mae_a = mean_absolute_error(actual, model_a)
mse_a = mean_squared_error(actual, model_a)
rmse_a = np.sqrt(mse_a)
r2_a = r2_score(actual, model_a)

# Calculate metrics for Model B
mae_b = mean_absolute_error(actual, model_b)
mse_b = mean_squared_error(actual, model_b)
rmse_b = np.sqrt(mse_b)
r2_b = r2_score(actual, model_b)
# Display Model A results
print("MODEL A PERFORMANCE")
print("-----------------------")
print(f"MAE  : {mae_a:.2f} mm")
print(f"MSE  : {mse_a:.2f} mm²")
print(f"RMSE : {rmse_a:.2f} mm")
print(f"R²   : {r2_a:.2f}")

# Display Model B results
print("\nMODEL B PERFORMANCE")
print("-----------------------")
print(f"MAE  : {mae_b:.2f} mm")
print(f"MSE  : {mse_b:.2f} mm²")
print(f"RMSE : {rmse_b:.2f} mm")
print(f"R²   : {r2_b:.2f}")
