#question 1--
import numpy as np
arr=np.array([
    [6, -8, 73, -110],
    [np.nan, -8, 0, 94]
])
print (arr)

arr_no_nan = np.nan_to_num(arr, nan=0)
print(arr_no_nan)

transposed = arr_no_nan.T
print(transposed)

#question 2--
arr = np.arange(24).reshape(2, 3, 4)
print(arr.shape)

new_arr = np.moveaxis(arr, 0, 2)
print(new_arr.shape)

new_arr = np.moveaxis(arr, [0, 1, 2], [2, 0, 1])
print(new_arr.shape)

#question3---
arr = np.array([
    [1, np.nan, 3],
    [4, 5, np.nan],
    [7, 8, 9]
])

print(arr)
col_means = np.nanmean(arr, axis=0)

inds = np.where(np.isnan(arr))

arr[inds] = np.take(col_means, inds[1])

print(arr)

#question 4---
arr = np.array([5, -2, 7, -9, 4])

arr[arr < 0] = 0

print(arr)

arr = np.array([5, -2, 7, -9, 4])

result = np.where(arr < 0, 0, arr)

print(result)

arr = np.array([5, -2, 7, -9, 4])

result = np.clip(arr, 0, None)

print(result)

