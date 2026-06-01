import numpy as np

# 1. Convert 1D array to 2D
arr1d = np.array([1, 2, 3, 4, 5, 6])
arr2d = arr1d.reshape(2, 3)
print("1D to 2D:\n", arr2d)

# 2. Print Array Attributes
print("\nArray Attributes:")
print("Shape:", arr2d.shape)
print("Dimension:", arr2d.ndim)
print("Data Type:", arr2d.dtype)
print("Item Size:", arr2d.itemsize)

# 3. Create a 3x3 NumPy array of all 9
arr_9 = np.full((3, 3), 9)
print("\n3x3 Array of 9s:\n", arr_9)

# 4. Create a 1D array of 10 evenly spaced values between 25 and 125
even_spaced = np.linspace(25, 125, 10)
print("\nEvenly Spaced Values:\n", even_spaced)

# 5. Convert a Python list into a NumPy array
py_list = [10, 20, 30, 40, 50]
np_array = np.array(py_list)
print("\nList to NumPy Array:\n", np_array)

# 6. Reverse a 1D NumPy array
arr = np.array([1, 2, 3, 4, 5])
print("\nReversed Array:\n", arr[::-1])

# 7. Create a 4x4x3 array and extract value at second set, first row, last column
arr_4x4x3 = np.arange(48).reshape(4, 4, 3)
print("\n4x4x3 Array:\n", arr_4x4x3)

value = arr_4x4x3[1, 0, 2]
print("\nSecond Set, First Row, Last Column:", value)

# 8. Create a 4x4 array and extract Odd Rows and Even Columns
arr4x4 = np.arange(1, 17).reshape(4, 4)
print("\n4x4 Array:\n", arr4x4)

odd_rows_even_cols = arr4x4[::2, 1::2]
print("\nOdd Rows and Even Columns:\n", odd_rows_even_cols)

# 9. Slice first two rows and first two columns of second set from 4x4x3 array
slice_array = arr_4x4x3[1, :2, :2]
print("\nSlice from Second Set:\n", slice_array)

# 10. Replace all odd numbers with -1 using for loop
arr_replace = np.array([[23, 56, 78, 93],
                        [71, 82, 13, 24]])

for i in range(arr_replace.shape[0]):
    for j in range(arr_replace.shape[1]):
        if arr_replace[i, j] % 2 != 0:
            arr_replace[i, j] = -1

print("\nReplace Odd Numbers with -1:\n", arr_replace)

# 11. Get indices of non-zero elements
arr_nonzero = np.array([1, 0, 2, 0, 3, 0, 4])
indices = np.nonzero(arr_nonzero)
print("\nIndices of Non-Zero Elements:", indices)

# 12. Arithmetic operations element-wise
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("\nAddition:\n", a + b)
print("Multiplication:\n", a * b)

# 13. Dot product of two arrays
arr1 = np.array([15, 20, 25])
arr2 = np.array([10, 40, 37])

dot_product = np.dot(arr1, arr2)
print("\nDot Product:", dot_product)