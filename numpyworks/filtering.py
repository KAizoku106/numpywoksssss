import numpy as np

productivity = np.array([
    [8, 7, 8, 6, 7, 8, 9, 8, 7, 8],
    [6, 7, 6, 7, 6, 7, 8, 7, 6, 7],
    [9, 8, 9, 8, 9, 9, 8, 9, 8, 9],
    [5, 6, 5, 6, 5, 6, 6, 5, 6, 5],
    [7, 8, 7, 8, 7, 8, 7, 8, 7, 8],
    [8, 9, 8, 9, 8, 9, 8, 9, 8, 9]
])

print(productivity[productivity<8])


#working hours between 5 to 7
print(productivity[(productivity<=7) & (productivity>=5)])

#first (coloumn )employee less than eight hour print
print((productivity[:,0])[(productivity[:,0])<8])

#print last two employees working hours  < 7
last_two_emp = productivity[:,-2:]
print(last_two_emp)
print(last_two_emp[last_two_emp<7])

#updata lessthan eight hours mark as 0

productivity[productivity<8]=0
print(productivity)