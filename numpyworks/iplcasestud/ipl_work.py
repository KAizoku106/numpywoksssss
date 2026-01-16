import numpy as np
#1. Load the CSV file using NumPy.
data= np.genfromtxt("numpyworks\\iplcasestud\\ipl.csv",delimiter=",",skip_header=1,filling_values=0,dtype="str")
print(data[0])
#2. Find the total number of matches played
print(np.count_nonzero(data[:,0].astype("int")))
#3. Extract all matches played in the 2023 season.
data2023= data[data[:,1]=="2023"]
print(data2023)
#4 Find the maximum and minimum runs scored by team_1.
team1runs=data[:,5].astype("int")
print(f"team1 max marks is {np.max(team1runs)}")
print(f"team1 min marks is {np.min(team1runs)}")

#5Calculate the average man_of_match_runs.
print(f"average man of the match run = {np.average(data[:,-2].astype("int"))}")

#6 Count how many matches were played at Wankhede
Wank= data[data[:,4]=="Wankhede"]
print(f"Wankhede matches = {np.count_nonzero(Wank[:,0]).astype("int")}")

#7 Display all matches where total_wickets > 15.

matchesgreater15= data[data[:,-1].astype("int")>15]
print(matchesgreater15)

#8 Find matches where team_1_runs > team_2_runs.
matchteamonegreaterteam2= data[data[:,5].astype("int")>data[:,6].astype("int")]
print(matchteamonegreaterteam2)

#9 Calculate the average total runs per match.
team2runs=data[:,6].astype("int")
avgruns= (team1runs+team2runs)/2
print("avrge",avgruns)

#10 Find how many matches CSK won.
cskwon= data[data[:,-3]=="CSK"]
print(f"no of winning matches of csk {np.count_nonzero(cskwon[:,0])}")

#11 Extract matches where RCB played (either team_1 or team_2)

rcbmatches = data[(data[:,2]=="RCB") | (data[:,3]=="RCB")]
print(rcbmatches)

#Find the season with the highest number of matches.
import collections
season=(data[:,1].astype("int"))
d= collections.Counter(season)
print(d)

#13 Get all matches where man_of_match_runs >= 75.
manofthematchgreater75 = data[data[:,-2].astype("int")>75]
print(manofthematchgreater75)

#14 Calculate the win percentage of MI.
mi_total= data[(data[:,2]=="MI") | (data[:,3]=="MI")]
mi_no_of_total_matches= np.count_nonzero(mi_total[:,0].astype("int"))
miwon= data[data[:,-3]=="MI"]
mi_number_won_matches= np.count_nonzero(miwon[:,0].astype("int"))
print(f"mi win percentage = {(mi_number_won_matches/mi_no_of_total_matches)*100}")

#15 Find matches played between MI vs CSK
mivscsk= data[((data[:,2]=="MI") & (data[:,3]=="CSK")) | ((data[:,2]=="CSK") & (data[:,3]=="MI")) ]
print("mi vs csk",mivscsk)

#16 Find the top 5 highest scoring matches (based on total runs).
total_match_run =np.array (team1runs+team2runs)
updated_data= np.column_stack((data,total_match_run))
#print(updated_data)
sorteddata=updated_data[np.argsort(updated_data[:,-1])]
print("top five highest total run matches",sorteddata[-1:-6:-1,:])

#17  Calculate the average wickets per season



#18  most common venue
venue = data[:,4]
ven,countvenue= np.unique(venue,return_counts=True)
print(countvenue)

        
vr= {i:v for i in ven for v in countvenue}
print(vr)



