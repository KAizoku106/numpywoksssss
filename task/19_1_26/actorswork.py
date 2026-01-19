import pandas as pd
df= pd.read_csv("task\\19_1_26\\malayalam_actors_actresses.csv")
print(df.head())
print(df.tail())
print(df.columns)
print(df.info())
print(df.isnull().sum())
print(df.count())

print(f"the average age of all the actors and actresses in the dataset {df["age"].mean()}")

df["career_span"]= 2025-df["debut_year"]
print(df.head())
print(f" those who have highest career span,print first three {df.sort_values(by="career_span",ascending=False).head(3)}")

print(f"hisghest number of award goes to {df.loc[df["no_of_awards"].idxmax()]}")

print(f"awards by birth place counts {df.groupby("place_of_birth")["no_of_awards"].sum()}")

df["debut_decade"]=df["debut_year"]-df["debut_year"]%10
#print(df.head())
print(f"debut decade wise average films number {df.groupby("debut_decade")["no_of_films"].mean()}")

# Have won more awards than the median of the entire dataset.

# Started their career after 1990.

# Are currently 'Active'.

# Have an age below 50

print(df[(df["no_of_awards"] > df["no_of_awards"].median()) & (df["active_status"]=="Active") & (df["age"]<50) & (df["debut_year"]> 1990 )])

