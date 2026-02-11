import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#Data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [25000, 27000, 30000, 28000, 32000, 31000]

#1. Line Chart using Matplotlib
plt.figure()
plt.plot(months,sales,marker='o')

plt.title("Monthly Sales (Line Chart)")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

#2. Bar Plot using Seaborn
#Converting to DataFrame(Seaborn works best with dataframe)
df=pd.DataFrame({
    "Month": months,
    "Sales": sales
})

plt.figure()
sns.barplot(x="Month", y="Sales", data=df)
plt.title("Monthly Sales (Bar Plot)")
plt.xlabel("Months")
plt.ylabel("Sales Amount")
plt.grid(True)
plt.show()