import numpy as np

numbers = np.array([10, 20, 30, 40])
print("Original array:", numbers)
print("Multiplied array:", numbers * 2)
# Topic 2: NumPy ndarray

# Create a 1D array
array_1d = np.array([10, 20, 30, 40])

# Create a 2D array
array_2d = np.array([[10, 20], [30, 40]])

print("1D Array:")
print(array_1d)

print("2D Array:")
print(array_2d)

print("Array Type:", type(array_1d))
# Topic 3: NumPy Array Creation

# Create an array with given values
array1 = np.array([10, 20, 30, 40])

# Create an array containing 5 zeros
array2 = np.zeros(5)

# Create an array containing 5 ones
array3 = np.ones(5)

# Create an array containing numbers from 1 to 10
array4 = np.arange(1, 11)

print("Normal Array:", array1)
print("Zeros Array:", array2)
print("Ones Array:", array3)
print("Range Array:", array4)

array1 = np.array([5, 10, 15, 20, 25])
array2 = np.zeros(4)
array3 = np.ones(4)
array5 = np.arange(1, 16)
print("Array1:", array1)
print("Array2:", array2)
print("Array3:", array3)
print("Array5:", array5)
numbers = np.array([[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120]])
print("Array:")
print(numbers)
print("Shape:", numbers.shape)
print("Dimensions:", numbers.ndim)
print("Data Type:", numbers.dtype)
import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print("First Element:", numbers[0])
print("Third Element:", numbers[2])
print("Last Element:", numbers[-1])
# Topic 5: 2D Array Indexing

numbers = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])

print("First Element:", numbers[0, 0])
print("Middle Element:", numbers[1, 1])
print("Last Element:", numbers[2, 2])
numbers = np.array([[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120]])
print("First value:", numbers[0, 0])
print("second value:", numbers[1, 2])
print("third value:", numbers[2, 1])
print("fourth value:", numbers[2, 3])
