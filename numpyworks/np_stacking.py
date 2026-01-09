import numpy as np
arr1=np.array([1,22,3,4])
arr2=np.array([10,20,30,40])

v_stack = np.vstack((arr1,arr2))
h_stack= np.hstack((arr1,arr2))

print(v_stack)
print(h_stack)