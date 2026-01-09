"""Rows represent employees and columns represent days (Day 1 to Day 10).

"""

import numpy as np

productivity = np.array([
    [8, 7, 8, 6, 7, 8, 9, 8, 7, 8],
    [6, 7, 6, 7, 6, 7, 8, 7, 6, 7],
    [9, 8, 9, 8, 9, 9, 8, 9, 8, 9],
    [5, 6, 5, 6, 5, 6, 6, 5, 6, 5],
    [7, 8, 7, 8, 7, 8, 7, 8, 7, 8],
    [8, 9, 8, 9, 8, 9, 8, 9, 8, 9]
])
"""1. Calculate the total number of hours worked by each employee over 10 days.
2. Calculate the total work hours for each day across all employees.
3. Find the average working hours per employee.
4. Find the average working hours per day.
5. Identify the employee index who worked the maximum total hours.
6. Identify the employee index who worked the minimum total hours.
7. Find the day index with the highest total working hours.
8. Identify employees who are overworked if average hours exceed 8 per day.
9. Calculate the difference between the most productive and least productive employee.
"""
#1 
print(f"total number of hours worked by each employee {np.sum(productivity,axis=1)}")

#4
print(f"  the total work hours for each day across all employees{np.sum(productivity,axis=0)}")


#3
print(f"average working hours of each employee {np.average(productivity,axis=1)}")

#4
print(f"the average working hours per day {np.average(productivity,axis=0)}")

#5
print(f"the employee index who worked the maximum total hours ={np.argmax(np.sum(productivity,axis=1))}")

#6
print(f"the employee index who worked the minimum total hours ={np.argmin(np.sum(productivity,axis=1))}")

#7
print(f"the day index which  the maximum total hours ={np.argmax(np.sum(productivity,axis=0))}")


#8
avrg=np.average(productivity,axis=1)
print(avrg)
print((avrg[avrg>8]))

#9 
print(f"{sum(np.max(productivity,axis=1))-sum(np.min(productivity,axis=1))}")
