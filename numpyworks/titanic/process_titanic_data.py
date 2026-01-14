import numpy as np
#np.genfromtxt(filepath,delimeter,skip_header,filling_values,dtype)
data = np.genfromtxt("numpyworks\\titanic\\passenger.csv",delimiter=",",skip_header=1,filling_values=0,dtype="str")
print(data.ndim)
print(data.size)
print(data.shape)

#survaival analysis
print(f"suvivied number={np.sum(data[:,1].astype("int"))}")
not_survived=np.count_nonzero(data[:,1].astype("int")==0)
survived=np.count_nonzero(data[:,1].astype("int")==1)

total = np.count_nonzero(data[:,0].astype("int"))

print("not suvived =",not_survived)
#survival_Rate
print((survived/total)*100,"survival rate")


#death rate
survived_unsruvived = data[:,1].astype("int")
unsurvived= survived_unsruvived[survived_unsruvived==0]
deathrate= (unsurvived.size /survived_unsruvived.size)*100

print(deathrate,"death rate")

#gender  analysis

#total number of males
gender= data[:,3]
print(f"total number of males= {gender[gender=="male"].size}")
print(f"total number of females= {gender[gender=="female"].size}")

male = data[data[:,3]=="male"]
female = data[data[:,3]=="female"]
print(male)
male_survival= np.count_nonzero(male[:,1].astype("int")==1)
female_survival= np.count_nonzero(female[:,1].astype("int")==1)
print(male_survival)
print(female_survival)


print(f"male survival rate {(male_survival/male[:,1].size)*100}")
print(f"female survival rate {(female_survival/female[:,1].size)*100}")
#survived male, two condition using
survived_males = data[(data[:,3]=="male") & data[:,1].astype("int")==1]
number_of_survival_males =survived_males[:,1].size
print(f"survived males are = {survived_males[:,1].size}")


#max age, min age, age analysis

min_age= np.max(data[:,-3].astype("int"))
max_age= np.min(data[:,-3].astype("int"))
ma= data[data[:,-3].astype("int")==np.max(data[:,-3].astype("int"))]
print(ma)
print(min_age,"min age")
print(f"min age ={max_age}")

#fare analysis

print(f"highest fare {np.max([data[:,-2].astype("float")])}")
print(f"lowest fare {np.min([data[:,-2].astype("float")])}")
print(f"average fare {np.average([data[:,-2].astype("float")])}")


#sort by fare, argsort give us index, so we give this index to data, so we got full data in sorted order of fare print(data[np.argsort(data[:,-2].astype("float"))])
print(data[np.argsort(data[:,-2].astype("float"))])

