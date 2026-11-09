import numpy as np

numbers = np.array([10, 20, 30, 40, 50, 60])

print("First three:", numbers[0:3])
print("Middle values:", numbers[2:5])
print("Every second:", numbers[::2])
# Topic 2: NumPy Reshape

numbers = np.array([10, 20, 30, 40, 50, 60])

reshaped_array = numbers.reshape(2, 3)

print("Original Array:", numbers)
print("Reshaped Array:")
print(reshaped_array)
print("New Shape:", reshaped_array.shape)
# Topic 3: Vectorized Operations

numbers = np.array([10, 20, 30, 40])

print("Original Array:", numbers)
print("Addition:", numbers + 5)
print("Subtraction:", numbers - 5)
print("Multiplication:", numbers * 2)
print("Division:", numbers / 2)
# Topic 4: NumPy Broadcasting

matrix = np.array([[1, 2, 3], [4, 5, 6]])

values = np.array([10, 20, 30])

result = matrix + values

print("Original Matrix:")
print(matrix)

print("Values:", values)

print("Broadcasting Result:")
print(result)
# Topic 5: NumPy Statistical Functions

numbers = np.array([10, 20, 30, 40, 50])

print("Original Array:", numbers)
print("Sum:", np.sum(numbers))
print("Mean:", np.mean(numbers))
print("Standard Deviation:", np.std(numbers))
numbers = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])
print("First Six Elements:", numbers[0:6])
print("Every Second Element:", numbers[::2])
reshaped_array = numbers.reshape(3, 4)
print("Reshaped array:", reshaped_array)
print("new shape:", reshaped_array.shape)
matrix = np.array([[10, 20, 30], [40, 50, 60]])
values = np.array([5, 10, 15])
print("Multiplication:", matrix * 2)
result = matrix + values
print("Broadcasting Result:", result)
print("Subtraction:", matrix - 5)
scores = np.array([65, 70, 75, 80, 85, 90, 95])
print("Sum:", np.sum(scores))
print("Mean:", np.mean(scores))
print("Standard Deviation:", np.std(scores))
print(scores > np.mean(scores))
print(np.sum(scores > np.mean(scores)))
