import pandas as pd
import numpy as np

#1. Loading CSV into DataFrame
df = pd.read_csv("sales.csv")

print("\nOriginal Data")
print(df)

#2. Addding new column "Total" = "Quantity * Price"
df["Total"] = df["Quantity"] * df["Price"]

print("\nData with Total column:")
print(df)

#3. Using numPy calculations
total_sales = np.sum(df["Total"])
average_daily_sales = np.mean(df["Total"])
std_dev_sales = np.std(df["Total"])

print("\nTotal Sales:", total_sales)
print("Average sales per day:", average_daily_sales)
print("Standard Deviation of Daily Sales:", std_dev_sales)

#4. Best-selling product (based on total quantity sold)
best_selling = df.groupby("Product")["Quantity"].sum()
best_product = best_selling.idxmax()

print("\nBest Selling Product:", best_product)

df.to_csv("sales.csv", index=False)#Adds the updated column to the csv file