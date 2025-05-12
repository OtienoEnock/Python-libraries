import pandas as pd
import sys
import matplotlib.pyplot as plt

data = pd.read_csv('Walmart_Sales.csv')
df = pd.DataFrame(data)

print(df.to_string()) #prints the whole dataset even if max rows is exceeded.
df.drop_duplicates() # remove duplicates.

df['Date'] = pd.to_datetime(df['Date'], format= 'mixed') #convert data type of the 'Date' column from 'object' to 'datetime'

#descriptive information about datase, first ten rows, and last five rows
#print(df.info())
print()
print(df.head(10))
print()
print(df.tail())

'''the dataset has the following properties:
1. three data types; int, float, and datetime
2. 6435 entries, range from index 0 to 6434
3. All entiries are valid, non-null (dataset is clean)'''

print(df.describe()) #obtain a quick analysis for each column

# data aggregation and analysis

sales_avg = df.groupby('Store', sort=True)['Weekly_Sales'].mean()

sales_avg.plot(kind='bar', width=0.8, color='green')
plt.title('Average sales per grossing store')
plt.xlabel('Stores')
plt.ylabel('Weekly Avegare sales')
plt.show()

#distribution of holidays.

holiday = df.groupby('Holiday_Flag')['Holiday_Flag'].count()
holiday.plot(kind='bar')
plt.title('Holidays')
plt.xlabel('Holiday: 1=True, 0=False')
plt.ylabel('day count')
plt.show()

#histogram for temperature.
plt.hist(df['Temperature'], bins=5)
plt.title('Temperature distribution')
plt.xlabel('Temperature')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()


#Show correlation between different columns. 
print(df.corr())