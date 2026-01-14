import numpy as np
import collections
collections.Counter
data=np.loadtxt("task\\13_1_26onlinestore\\onlinestore.csv",delimiter=",",skiprows=1,dtype="str")
#print(data)
print(f"shape of data={data.ndim}")
id= data[:,0].astype("int")
print(f"total number of orders={np.max(id)}")
all_unit_price = data[:,-4].astype("int")
print(f"unit price average = {np.average(all_unit_price)}")
perorder_revenue = data[:,-5].astype("int") * data[:,-4].astype("int")
print(f"total revenue per order{perorder_revenue}")
#Find orders with delivery days > 5
print(f"orders with delivary days greater than five {data[data[:,-2].astype("int")>5]}")
#Count returned vs non-returned orders
c=list(data[:,-1])
d=collections.Counter(c)
print(d)
returned=data[data[:,-1]=="Yes"]
not_returned=data[data[:,-1]=="No"]
print(f"returened {len(returned)}:not returned {len(not_returned)}")

product_category =  np.unique(data[:,2])
#print(product_category)
for i in product_category:
    dis=data[data[:,2]==i]
    
    print(f"average discount of {i} category = {np.average([dis[:,-3].astype("int")])}")


delivary_mode= np.array(np.where(data[:,-2].astype("int")<=3,"Fast","Normal"))
updated_data= np.column_stack((data,delivary_mode))
#print(updated_data)


