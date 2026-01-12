# 2D Array Practice

# 9. Let arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]). Extract the first row.


# 10. From the same array, extract the last column.


# 11. From arr = np.array([[2, 4, 6], [8, 10, 12], [14, 16, 18]]), select elements greater than 10.


# 12. Use advanced indexing to select elements at positions (0,0), (1,1), and (2,2) from the above array.


# 13. Given arr = np.array([[1, 2], [3, 4], [5, 6]]), multiply every element by 5 using broadcasting.


# 14. From arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]), extract the subarray [[3,4],[7,8]].


# 15. Given arr = np.array([[2, 4], [6, 8], [10, 12]]), multiply only the first column by 10 using broadcasting.

import numpy as np
"""9"""
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr[0])
"""10"""
print(arr[:,-1])
"""11"""
arr = np.array([[2, 4, 6], [8, 10, 12], [14, 16, 18]])
print(arr[arr>10])

"""12"""
print(arr[[0, 1, 2], [0, 1, 2]])

"""13"""
arr = np.array([[1, 2], [3, 4], [5, 6]])
print(arr*5)

"""14"""
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(arr)
print(arr[0:2,2:])

"""15"""
arr = np.array([[2, 4], [6, 8], [10, 12]])
arr[:,0]=arr[:,0]*10
print(arr)