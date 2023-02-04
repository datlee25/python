import numpy as np

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
#
# newarr = arr.reshape(2,3,2)
# flatarr = newarr.reshape(-1)
#
# print(newarr)
# print(flatarr)

# arr1 = np.array([1, 2, 3])
#
# arr2 = np.array([4, 5, 6])
# #
# arrstack = np.stack((arr1, arr2), axis=0)
# arrconcat = np.concatenate((arr1,arr2), axis=0)
# print("Stack: ", arrstack)
# print("Concatenate: ", arrconcat)
# Stack:  [[1 2 3]
#  [4 5 6]]
# Concatenate:  [1 2 3 4 5 6]

a = np.array([[1, 2], [3, 4]])
# Mang b
b = np.array([[5, 6], [7, 8]])
arrconcat = np.concatenate((a, b), axis=1)
arrstack = np.stack((a, b), axis=1)
#
# print(arrstack)
# print(arrstack)
# Stack:  [[[1 2]
#   [3 4]]
#
#  [[5 6]
#   [7 8]]]
# Concatenate:  [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]
#
# arr1 = np.array([1, 2, 3])
#
# arr2 = np.array([4, 5, 6])
#
# a = np.array([[1, 2], [3, 4]])
# # Mang b
# b = np.array([[5, 6], [7, 8]])
# arr = np.vstack((a, b))
# print(arr)
# a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# ar = np.diag(a)
# x = np.diag([1,3,4,4,56,65])
# print(x)
# print(ar)
