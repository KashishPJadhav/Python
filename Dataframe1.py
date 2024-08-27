import pandas as pd
df=pd.DataFrame({'Name':[],'Age':[],'City':[]})
nname=[] # Initialize lists to store new data
nage=[]
ncity=[]
a=int(input("Number of entries : "))
for i in range(a):
  name_input = input("Enter Name : ")  # Store input in temporary variables
  age_input = int(input("Age : "))
  city_input = input("City : ")
  nname.append(name_input)  # Append to the lists
  nage.append(age_input)
  ncity.append(city_input)
newd=pd.DataFrame({
    'Name':nname,
    'Age' :nage,
    'City':ncity,
})
df=pd.concat([df,newd])
print(df)