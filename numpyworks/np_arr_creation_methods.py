"""array creation methods
np.array()
np.zeros()
np.ones()
np.full()

"""
import numpy as np

zeros_array = np.zeros((3,3),dtype="int16")
print(zeros_array)

ones_array = np.ones((5,5),dtype=int)
print(ones_array)
#full array with element 8
print(np.full((5,5),8))