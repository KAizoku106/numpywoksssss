import numpy as np

attendance = [
  
  #m  t  w  h  f
  [1, 1, 1, 1, 1], # Student 1
  [1, 0, 1, 1, 1], # Student 2
  [1, 1, 0, 1, 1], # Student 3
  [0, 1, 1, 1, 0], # Student 4
  [1, 1, 1, 0, 1], # Student 5
  [1, 0, 0, 1, 1], # Student 6
  [1, 1, 1, 1, 0], # Student 7
  [0, 1, 1, 0, 1], # Student 8
  [1, 1, 0, 1, 0], # Student 9
  [1, 0, 1, 1, 1]  # Student 10
#   

]
"""fuctions
-------------
sum,max,min,avg
axis=0  --->coloum
axis=1 ----->row

"""

arr= np.array(attendance)
print(arr)

#update a value

arr[0,1]=0
print(arr)

#row wise sum
print(np.sum(arr,axis=1))

#coloum wise sum
print(np.sum(arr,axis=0))

#count of zeros in each row or students absent count
print(5-(np.sum(arr,axis=1)))
print(np.count_nonzero(arr==0,axis=1))
#count of zeros in each coloumn or day absent count

print(np.count_nonzero(arr==0,axis=0))