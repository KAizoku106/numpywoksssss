import numpy as np

leads = np.array([
    # s  m    t  w   th
    [12, 18, 10, 15, 5],   # facebook
    [20, 25, 22, 18, 8],   # insta
    [18, 30, 25, 22, 10],  # youtube
    [25, 28, 30, 26, 12],  # refferal
    [30, 35, 28, 32, 15],  # walkin
    [40, 45, 38, 40, 20],  # reddit
    [35, 50, 42, 45, 25]   # camp
    
])
#1 each day lead sum
print(np.sum(leads,axis=0))

# 2 task2 total leads from each sourece in  7  days
print(np.sum(leads,axis=1))

#tas3 highest lead day

print(np.argmax(np.sum(leads,axis=0)))

#task4 average leads per source

print(np.average(leads,axis=1))

#5 average leads per day

print(np.average(leads,axis=0))

#highest lead source

print(np.argmax(np.sum(leads,axis=1)))
print((np.sum(leads,axis=1)))