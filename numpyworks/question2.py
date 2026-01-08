import numpy as np
four_arr= np.full((5,5),4)
one_arr= np.ones((3,3))
one_arr[1,1]=100
four_arr[1:4,1:4]=one_arr
print(four_arr)