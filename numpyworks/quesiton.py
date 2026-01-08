import numpy as np
seven_array = np.full((5,7),7)
print(seven_array)
seven_array[1:4,2:5]=0
print(seven_array)
seven_array[2,3]=1
print(seven_array)
