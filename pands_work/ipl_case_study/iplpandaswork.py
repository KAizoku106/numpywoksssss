import pandas as pd
df=pd.read_csv("pands_work\\ipl_case_study\\ipl_data.csv")
print(df.head())
print(df.columns)

print(df.shape)
print()
print(df.info())
print(df.isnull().sum())

df["match_id"].fillna(df["match_id"].shift(-1) - 1 ,inplace= True) 
df["match_id"].fillna(df["match_id"].shift(-2) - 2, inplace= True)
print(df.isnull().sum())

df["season"].fillna(df["season"].mode()[0],inplace=True)
print(df.isnull().sum())
df["city"].fillna(df["city"].mode(),inplace=True)
print(df.isnull().sum())
df["team1"].fillna("unknown",inplace=True)
print(df.isnull().sum())
df["team2"].fillna("unknown",inplace=True)
print(df.isnull().sum())
df["winning_team"].fillna("unknown",inplace=True)
print(df.isnull().sum())
df["player_of_match"].fillna("unknown",inplace=True)
print(df.isnull().sum())
df["venue"].fillna(df["venue"].mode()[0],inplace=True)
print(df.isnull().sum())
df["city"].fillna(df["city"].mode()[0],inplace=True)
print(df.isnull().sum())
df["runs_scored"].fillna(df["runs_scored"].mean(),inplace=True)
print(df.isnull().sum())
df["wickets"].fillna(df["wickets"].mean(),inplace=True)
print(df.isnull().sum())

print("matches per season",df["season"].value_counts())

print("top match  count season" ,df["season"].value_counts().idxmax())


print(f"total match won by each team {df["winning_team"].value_counts()}")

print(f"average  runs per each team {df.groupby("season")["runs_scored"].mean()}")

print(f" venue vise count {df["venue"].value_counts()}")

print(f"venue wise average run {df.groupby("venue")["runs_scored"].mean()}")

print(f"city wise match count {df['city'].value_counts()}")
print(F"city wise average runs {df.groupby("city")["runs_scored"].mean()}")

print(df.head())

print(f"team with highest average run {df.groupby("winning_team")["runs_scored"].mean().idxmax()}")

print(f"top 3 venue {df["venue"].value_counts().head(3)}")
