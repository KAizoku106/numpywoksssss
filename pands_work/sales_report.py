sales_report = [
    {"date": "2026-01-01", "product": "Laptop", "category": "Electronics", "quantity": 2, "price": 55000, "salesperson": "Anil"},
    {"date": "2026-01-01", "product": "Mouse", "category": "Electronics", "quantity": 5, "price": 500, "salesperson": "Meera"},
    {"date": "2026-01-02", "product": "Chair", "category": "Furniture", "quantity": None, "price": 3500, "salesperson": "Rahul"},
    {"date": "2026-01-02", "product": "Desk", "category": "Furniture", "quantity": 1, "price": None, "salesperson": "Rahul"},
    {"date": "2026-01-03", "product": "Pen", "category": "Stationery", "quantity": 20, "price": 10, "salesperson": None},
    {"date": "2026-01-03", "product": "Notebook", "category": "Stationery", "quantity": 10, "price": 50, "salesperson": "Anil"},
    {"date": None, "product": "Printer", "category": "Electronics", "quantity": 1, "price": 12000, "salesperson": "Meera"},
    {"date": "2026-01-04", "product": "Monitor", "category": "Electronics", "quantity": 2, "price": None, "salesperson": "Anil"},
    {"date": "2026-01-05", "product": None, "category": "Furniture", "quantity": 1, "price": 8000, "salesperson": "Rahul"},
    {"date": "2026-01-05", "product": "Table Lamp", "category": None, "quantity": 3, "price": 1500, "salesperson": "Meera"}
]
import pandas as pd
df= pd.DataFrame(sales_report)

print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.info())
print(df.isnull().sum())

most_frequent_date= df["date"].mode()[0]
df["date"].fillna(most_frequent_date,inplace=True)
print(df.isnull().sum())
df["product"].fillna("unknown",inplace=True)
#print(df)
frequnet_category = df["category"].mode()[0]
df["category"].fillna(frequnet_category,inplace=True)
print(df)

# df["quantity"].fillna(df.groupby("category")["quantity"].transform("mean"),inplace=True)
# print(df)


most_price= df["price"].mean()
df["price"].fillna(most_price,inplace=True)

df.dropna(subset=["salesperson"],inplace=True)
print(df)

#sale count by category
print(df["category"].value_counts())
print(df["salesperson"].value_counts())

print(df[(df["category"]=="Electronics") & (df["quantity"]>2)])

#group by
print(df.groupby("category")["price"].sum())

print(df.groupby("category")["quantity"].sum())

print(df.groupby("salesperson")["price"].sum())


print(df.sort_values(by="price",ascending=False))

#loc and iloc
print(df.loc[2])
print(df.iloc[5])

print(df[df["price"]==df["price"].max()])
print(df[df["price"]==df["price"].min()])

print(df.loc[df["price"].idxmin()])
print(df.info())

#add new coloumn
df["revenue"]=df["price"]*df["quantity"]
print(df)

#zeroth index name and category

print(df.loc[1,["product","salesperson"]])