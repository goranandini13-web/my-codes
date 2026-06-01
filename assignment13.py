#question 1---
import numpy as np

arr = np.array([[6, -8, 73, -110],
                [np.nan, -8, 0, 94]])

# Replace NaN with 0
arr = np.nan_to_num(arr, nan=0)

print("After replacing NaN:")
print(arr)

# Interchange rows and columns (Transpose)
transposed = arr.T

print("\nTranspose:")
print(transposed)

#quesstion2--
import numpy as np

arr = np.arange(24).reshape(2,3,4)

print("Original Shape:", arr.shape)

new_arr = np.moveaxis(arr, 0, 2)

print("New Shape:", new_arr.shape)
print(new_arr)

#question3---
import numpy as np

arr = np.array([[10, np.nan, 30],
                [40, 50, np.nan],
                [70, 80, 90]])
# Column means
col_mean = np.nanmean(arr, axis=0)

# Find NaN positions
inds = np.where(np.isnan(arr))

# Replace NaN with column mean
arr[inds] = np.take(col_mean, inds[1])

print(arr)

#question4--
import numpy as np
arr = np.array([10, -5, 20, -8, 30, -2])
arr[arr < 0] = 0
print(arr)

#question6--
import numpy as np

A = np.array([[1, -2, 3],
              [-1, 3, -1],
              [2, -5, 5]])

B = np.array([9, -6, 17])

solution = np.linalg.solve(A, B)

print("x =", solution[0])
print("y =", solution[1])
print("z =", solution[2])

#question7--
import matplotlib.pyplot as plt
import numpy as np

subjects = ['Math', 'Physics', 'Chemistry',
            'English', 'Computer']

sem1 = [78, 82, 75, 85, 90]
sem2 = [88, 85, 80, 87, 95]

x = np.arange(len(subjects))
width = 0.35

plt.figure(figsize=(10,6))

plt.bar(x - width/2, sem1,
        width,
        color='skyblue',
        label='Semester 1')

plt.bar(x + width/2, sem2,
        width,
        color='orange',
        label='Semester 2')

plt.title('Semester Result Comparison',
          fontsize=16,
          color='darkblue')

plt.xlabel('Subjects')
plt.ylabel('Marks')
plt.xticks(x, subjects)

plt.grid(axis='y',
         linestyle='--',
         alpha=0.7)

plt.legend()
plt.show()