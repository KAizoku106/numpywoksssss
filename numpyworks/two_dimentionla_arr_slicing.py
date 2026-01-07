import numpy as np

arr = np.array([
    [33,31,27],
    [31,30,29],
    [33,32,34]

])

print(arr.ndim)
print(arr.size)
print(arr.shape)

# print first row

print(arr[0])
 
#print last row
print(arr[2]) 

#print second and thrid row
print(arr[1:3])

#fetching row from zero to one 
print(arr[0:2])


#print  all row and 2 and 3 coloums 

print(arr[:,1:3])

#print(all rows and its second coloum)
print(arr[:,1:2])
print(arr[:,1])

#print thrid row second column value
print(arr[2,1])


print(arr[1:,1:])