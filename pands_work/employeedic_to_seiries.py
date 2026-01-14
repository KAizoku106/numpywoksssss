import pandas as pd
employee_and_itsdepartment= {1:15,2:45,3:56,4:55}
series = pd.Series(employee_and_itsdepartment)
#print(series)

#aggregate functions
#sum,max,min,mean

print(series.sum)
print(f"max ={series.max()}")
print(f"min ={series.min()}")
print(f"avg ={series.mean()}")
