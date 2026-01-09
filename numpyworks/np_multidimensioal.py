import numpy as np
sales_report = np.array([
    [
        [10,11],
        [12,13]
    ],
    [
        [20,30],
        [50,40]
        
    ]
])
print(sales_report)
print(sales_report.ndim)

print(sales_report[1,0,0])

(sales_report[1,1,1])=80

print(sales_report)