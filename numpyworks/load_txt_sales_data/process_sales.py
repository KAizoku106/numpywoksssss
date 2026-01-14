import numpy as np

#syntas
#np.loadtxt(filepath,delimeter=,skip_rows=)
data = np.loadtxt("numpyworks\\load_txt_sales_data\\sales.csv",delimiter=",",skiprows=1,dtype="str")
# print(data)
# print(data.ndim)
# #print(np.sum(int(data[:,3])))
# quantities=(data[:,3]).astype("int")
# print(f"total quantities = {np.sum(quantities)}")

# print(f"maximum unit solded ={np.max(quantities)}")

# print(f"min unit solded = {np.min(quantities)}")

# print(f"avg unit solded = {np.average(quantities)}")

# revenue = data[:,3].astype("int") *  data[:,4].astype("int")
# print("individual revenue",revenue)
# print(f" total revenue = {np.sum(revenue)}")


# print(data[data[:,3].astype("int")>8])

# print(data[data[:,2]=="Electronics"])

#all products give a hundred rupees discount

data[:,-2]=data[:,-2].astype("int")-100
print("discount ",data)

north = data[data[:,-1]=="North"]
print(north)
revenue_north = north[:,3].astype("int") *  north[:,4].astype("int")
print(revenue_north)
total_rev_nort = np.sum(revenue_north)
print(total_rev_nort)



