import numpy as np
arr_two_d_1=[
    [1,2],
    [3,4]
]
arr_two_d_2=[
    [10,20],
    [30,40]
]

v_stack = np.vstack((arr_two_d_1,arr_two_d_2))

h_stack = np.hstack((arr_two_d_1,arr_two_d_2))

print(v_stack)
print(h_stack)