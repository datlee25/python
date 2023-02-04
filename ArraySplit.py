import numpy as np

# TODO: Split 1-D arrays with the number of splits
arr = np.array([1, 2, 3, 4, 5, 6])
newArr = np.array_split(arr, 3)
# print(newArr)
# Result is : [array([1, 2]), array([3, 4]), array([5, 6])]

# TODO: Split 1-D arrays but it's elements less then required
arr = np.array([1, 2, 3, 4, 5, 6])
newArr = np.array_split(arr, 4)
# print(newArr)
# Result : [array([1, 2]), array([3, 4]), array([5]), array([6])]

# TODO: Compare split() and array_split()
arr = np.array([1, 2, 3, 4, 5, 6])
# newArr1 = np.split(arr,4)
newArr2 = np.array_split(arr, 4)

# print(newArr1)
# print(newArr2[0], newArr2[1], newArr2[2], newArr2[3])
# NOTE: So when the array has less elements than required:
#   split() : log error
#   array_split(): worked properly

# TODO: Split 2-D arrays with the number of splits
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newArr = np.array_split(arr, 3)
# print(newArr)
# Result : [array([[ 1,  2],
            #      [ 3,  4],
            #      [ 5,  6],
            #      [ 7,  8],
            #      [ 9, 10],
            #      [11, 12]])]

# TODO: Split the 2-D array into three 2-D arrays along row
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newArr = np.array_split(arr, 3, axis=1)
print(newArr)

# TODO: Use the hsplit() method to split the 2-D array into three 2-D arrays along rows
arr = np.array([[ 0.,   1.,   2.,   3.],
       [ 4.,   5.,   6.,   7.],
       [ 8.,   9.,  10.,  11.],
       [12.,  13.,  14.,  15.]])
# newArr = np.vsplit(arr, 2)
# print(arr)
# print(newArr)
