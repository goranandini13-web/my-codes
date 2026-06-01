#question1---
import numpy as np

arr1 = np.array([10, 20, 30])       
arr2 = np.array([[40, 50, 60]])     
result = np.vstack((arr1, arr2))
print(result)

#question2---
import numpy as np
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
flat = arr.flatten()

print(flat)

#question 3---
import numpy as np
arr = np.array([10, 20, 30, 40, 50])
print(arr[::-1])

#question4--     maximum value
import numpy as np
arr = np.array([10, 25, 5, 40])
print(np.max(arr))
print(np.min(arr))

#no. of rows and columns
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
rows, cols = arr.shape
print("Rows =", rows)
print("Columns =", cols)

#select every element
for row in arr:
    for value in row:
        print(value)

#sum of values using for loop
arr = np.array([[1, 2],
                [3, 4]])
total = 0
for row in arr:
    for value in row:
        total += value
print(total)

#array airthmetic
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

#question5---
import numpy as np
arr = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])
for matrix in arr:
    for row in matrix:
        for value in row:
            print(value)

#using nditer
import numpy as np
arr = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])
for value in np.nditer(arr):
    print(value)

 #question6---
import numpy as np
arr1 = np.array([[1, 2],
                 [3, 4]])
arr2 = np.array([[5, 6],
                 [7, 8]])

#Average of Two Arrays
avg = (arr1 + arr2) / 2
print(avg)

#Mean
combined = np.concatenate((arr1.flatten(),
                           arr2.flatten()))

print(np.mean(combined))

#Median
print(np.median(combined))

