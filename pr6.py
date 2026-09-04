import numpy as np

# 1. Array Creation
a = np.array([10, 20, 30, 40, 50, 60])

print("Original Array:")
print(a)

# 2. Indexing
print("\nIndexing:")
print("First element:", a[0])
print("Third element:", a[2])

# 3. Slicing
print("\nSlicing:")
print("First three elements:", a[:3])
print("Last three elements:", a[3:])

# 4. Reshaping
b = a.reshape(2, 3)

print("\nReshaped Array (2 x 3):")
print(b)

# 5. Mathematical Operations
print("\nMathematical Operations:")

print("Addition by 5:")
print(a + 5)

print("Subtraction by 5:")
print(a - 5)

print("Multiplication by 2:")
print(a * 2)

print("Division by 2:")
print(a / 2)

print("Square of each element:")
print(a ** 2)

# 6. Basic Mathematical Functions
print("\nBasic Mathematical Functions:")
print("Sum:", np.sum(a))
print("Mean:", np.mean(a))
print("Maximum:", np.max(a))
print("Minimum:", np.min(a))