import pandas as pd

students={
    "name":["adhnan","adhil","mesin","hafi"],
    "age":[21,21,24,24],
    "course":["ds","ds","ds","django"]
    }
db= pd.DataFrame(students)
print(db)
print(db[1:2])

print(db["course"])

print(db[["name","course"]])
print(db[["name","age"]])

