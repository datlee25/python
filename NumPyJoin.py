import numpy as np

# TODO: Concatenate two one-dimensional array with axis = 0
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
# print(np.concatenate((arr1, arr2)))
# Result is : [1 2 3 4 5 6]

# TODO: Concatenate two multi-dimensional array with axis = 0
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
# print(np.concatenate((arr1, arr2), axis=0))
# Result is : [[1 2]
            #  [3 4]
            #  [5 6]
            #  [7 8]]

# TODO: Concatenate two multi-dimensional array with axis = 1
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
# print(np.concatenate((arr1, arr2), axis=1))
# Result is : [[1 2 5 6]
#              [3 4 7 8]]

# TODO: Stack two one-dimensional array with axis = 0
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
# print(np.stack((arr1, arr2), axis=0))
# Result is : [[1 2 3]
#              [4 5 6]]

# TODO: Stack two multi-dimensional array with axis = 0
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
# print(np.stack((arr1, arr2), axis=0))
# Result is : [[[1 2]
            #   [3 4]]
            #
            #  [[5 6]
            #   [7 8]]]

# TODO: Stack two multi-dimensional array with axis = 1
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
# print(np.stack((arr1, arr2), axis=1))
# Result is : [[[1 2]
            #   [5 6]]
            #
            #  [[3 4]
            #   [7 8]]]

# TODO: HStack two one-dimensional array
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
# print(np.hstack((arr1, arr2)))
# Result is : [1 2 3 4 5 6]

# TODO: HStack two multi-dimensional array
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
# print(np.hstack((arr1, arr2)))
# Result is : [[1 2 5 6]
#              [3 4 7 8]]

# TODO: VStack two one-dimensional array
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
# print(np.vstack((arr1, arr2)))
# Result is : [[1 2 3]
#              [4 5 6]]

# TODO: VStack two multi-dimensional array
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
# print(np.vstack((arr1, arr2)))
# Result is : [[1 2]
            #  [3 4]
            #  [5 6]
            #  [7 8]]

# TODO: DStack two one-dimensional array
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
# print(np.dstack((arr1, arr2)))
# Result is : [[1 2 3]
#              [4 5 6]]

# TODO: DStack two multi-dimensional array
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
# print(np.vstack((arr1, arr2)))
# Result is : [[1 2]
            #  [3 4]
            #  [5 6]
            #  [7 8]]

