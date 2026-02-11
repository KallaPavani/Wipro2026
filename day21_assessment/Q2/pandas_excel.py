import pandas as pd

#1. Read Excel File
df=pd.read_excel("sales_data.xlsx", sheet_name="2025")

#2. Add total Column
df["Total"]=df["Quantity"]*df["Price"]

#3. Save to new Excel File
df.to_excel("sales_summary.xlsx", index=False)

print("Sales summary file created successfully!")
