import pandas as pd
from datetime import datetime
date_range = pd.date_range(start='2024-01-10 ', periods=6, freq='M')
df = pd.DataFrame(date_range, columns=['Date'])

print("Date range : \n",df)
print("\n------------------------------------------\n")
df=pd.DataFrame({
    'Time': date_range.time,
    'A':['A1','A2','A3','A4','A5','A6'],
    'B':['B1','B2','B3','B4','B5','B6']
    },index=date_range)
df.index.name='index'
print(df)
print("\n--------------------------------------------\n")
date_range = pd.date_range(start='2024-01-10 12:30:00', periods=6, freq='M')

df=pd.DataFrame({
    'A':['A1','A2','A3','A4','A5','A6'],
    'B':['B1','B2','B3','B4','B5','B6']
    },index=date_range)
df.index.name='Date      Time '
print(df)
d = input("Enter birth date (YYYY-MM-DD): ")
db=datetime.strptime(d,'%Y-%m-%d')
print(db)
age=datetime.now()-db
print("Age is : ",age)

y=age.days/365
print("in years : ",int(y))
