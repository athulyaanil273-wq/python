# Program to create different arrays using NumPy and Pandas

import numpy as np
import pandas as pd

# ---------------- NUMPY ARRAYS ----------------

# 1D Array
arr1 = np.array([1, 2, 3, 4, 5])
print("NumPy 1D Array:")
print(arr1)

# 2D Array
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])
print("\nNumPy 2D Array:")
print(arr2)

# 3D Array
arr3 = np.array([[[1, 2], [3, 4]],
                 [[5, 6], [7, 8]]])
print("\nNumPy 3D Array:")
print(arr3)

# Zero Array
zero_arr = np.zeros((2, 3))
print("\nNumPy Zero Array:")
print(zero_arr)

# Ones Array
ones_arr = np.ones((3, 3))
print("\nNumPy Ones Array:")
print(ones_arr)

# Full Array
full_arr = np.full((2, 2), 7)
print("\nNumPy Full Array:")
print(full_arr)


# ---------------- PANDAS ARRAYS ----------------

# 1D Array using Series
p1 = pd.Series([1, 2, 3, 4, 5])
print("\nPandas 1D Array:")
print(p1)

# 2D Array using DataFrame
p2 = pd.DataFrame([[1, 2, 3],
                   [4, 5, 6]])
print("\nPandas 2D Array:")
print(p2)

# 3D Array using Panel-like structure (Dictionary of DataFrames)
p3 = {
    "Layer1": pd.DataFrame([[1, 2], [3, 4]]),
    "Layer2": pd.DataFrame([[5, 6], [7, 8]])
}
print("\nPandas 3D Array:")
for key, value in p3.items():
    print(f"\n{key}")
    print(value)

# Zero Array using DataFrame
p_zero = pd.DataFrame(np.zeros((2, 3)))
print("\nPandas Zero Array:")
print(p_zero)

# Ones Array using DataFrame
p_ones = pd.DataFrame(np.ones((3, 3)))
print("\nPandas Ones Array:")
print(p_ones)

# Full Array using DataFrame
p_full = pd.DataFrame(np.full((2, 2), 9))
print("\nPandas Full Array:")
print(p_full)
