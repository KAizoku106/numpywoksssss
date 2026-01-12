# ✅ 1D Array Practice

# 1. Given arr = np.array([3, 6, 9, 12, 15, 18]), extract the 3rd element.


# 2. From arr = np.array([5, 10, 15, 20, 25, 30]), extract elements from index 2 to 4.


# 3. Given arr = np.array([2, 4, 6, 8, 10, 12]), extract all even-indexed elements.


# 4. From arr = np.array([11, 22, 33, 44, 55]), select elements greater than 30.


# 5. Given arr = np.array([7, 14, 21, 28, 35]), replace all numbers greater than 20 with -1.


# 6. From arr = np.array([1, 2, 3, 4, 5]), pick elements at positions [0, 2, 4] using advanced indexing.


# 7. Let arr = np.array([10, 20, 30, 40]). Multiply every element by 2 using broadcasting.


# 8. Given arr = np.array([100, 200, 300, 400, 500]), reverse the array using advanced indexing.




# ---

# ✅ 2D Array Practice

# 9. Let arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]). Extract the first row.


# 10. From the same array, extract the last column.


# 11. From arr = np.array([[2, 4, 6], [8, 10, 12], [14, 16, 18]]), select elements greater than 10.


# 12. Use advanced indexing to select elements at positions (0,0), (1,1), and (2,2) from the above array.


# 13. Given arr = np.array([[1, 2], [3, 4], [5, 6]]), multiply every element by 5 using broadcasting.


# 14. From arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]), extract the subarray [[3,4],[7,8]].


# 15. Given arr = np.array([[2, 4], [6, 8], [10, 12]]), multiply only the first column by 10 using broadcasting.




# -
import numpy as np
# arr = np.array([3, 6, 9, 12, 15, 18])
# print(arr[2])

# print("2")
# arr = np.array([5, 10, 15, 20, 25, 30])
# print(arr[1:4])
"""3"""
# arr = np.array([2, 4, 6, 8, 10, 12])
# print(arr[::2])
"""4"""
arr = np.array([11, 22, 33, 44, 55])
print(arr[arr>30])

"""5"""
arr = np.array([7, 14, 21, 28, 35])
arr[arr>20]=-1
print(arr)

"""6"""
arr = np.array([1, 2, 3, 4, 5])
print(arr[:5:2])

"""7"""
arr = np.array([10, 20, 30, 40])
print(arr*2)


"""8"""
arr=np.array([100, 200, 300, 400, 500])

print(arr[::-1])