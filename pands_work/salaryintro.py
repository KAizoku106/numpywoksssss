import pandas as pd
salary= [ 30000,34000,40000,50000,60000]
series = pd.Series(salary,index=["e1","e2","e3","e4","e5"])
# print(salary[0])
# print(salary[1:3])
print(series["e3"])
print(series["e2":"e5"])

