import numpy as np
import pandas as pd
arr=np.array([10,20,5,6,200])

print("array:", arr)
print("sum",np.sum(arr))
print("mean",np.mean(arr))
print("max",np.max(arr))
print("min",np.min(arr))
print("multiply by 2:", arr*2)

data={
    "Name":["kiran","Anita","Ravi"],
    "Age":[21,27,24],
    "City":["Bangalore", "Chennai","Hyderabad"]
}

df=pd.DataFrame(data)
print(df)

print(df["Name"])

print(df[df["Age"]>26])
df["Salary"]=[50000,60000,70000]
print(df)