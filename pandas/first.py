import pandas as pd 
import numpy as np

# deta = { "Name" : ["Abhay" , "Rahul" , "Patil"] ,
#         "Age" : [10,20,30] ,
#         "Salary" : [ 15000 , 54500 , 56000 ]
#         }

# df = pd.DataFrame(deta)

# print(df)

# data = pd.read_csv("Path of file")
# For csv

# data = pd.read_excel(r"C:\Users\WIN10\Desktop\Data analytics\Online Retail.xlsx")
# For exel

# print(data)

data = pd.read_excel(r"C:\Users\WIN10\Desktop\Data analytics\SalesData.xlsx")

# print(data)

# print(data.head(10)) #default value 5
# print(data.tail(10))

# print(data.info())

# print(data.describe())

# print(data.isnull())
# print(data.isnull().sum())

# print(data.duplicated())
# print(data["Units"].duplicated())
# print(data["Units"].duplicated().sum())


# data = data.drop_duplicates("Units")
# print(data)

# print(data.isnull().sum())

# print(data["Units"].dropna())

# # print(data.replace(np.nan,"hi"))

# print(data)

# print(data["Units"].replace(np.nan , 15000))

# print(data["Units"].mean())

# print(data.fillna(method = "bfill"))

# print(data)

# data.loc[(data["Units"] < 10 ) , "GetsBonus"] = "no bonus"; 
# data.loc[(data["Units"] > 10 ) , "GetsBonus"] = "bonus"; 

# data["fullname"] = data["Region"] + " "+ data["Rep"]
# print(data)

# print(data)


# data["salary"] = data["Units"] * 100000 
# print(data)

# data["Bonus"] = ( data["salary"] / 100 ) * 20 
# print(data)

# Group by

data = pd.read_excel(r"C:\Users\WIN10\Desktop\Data analytics\employee_data.xlsx")

# print(data.head(10))

# data['High Salary'] = data["salary"] > 10000  # Create a boolean column
# gd = data.groupby(['Performance Rating', 'High Salary']).size().reset_index(name='count')
# print(gd)

data1 = {
    "EmpId" : [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 ] ,
    "EmpName" : ["abhay" ,"rahul" , "mukesh" , "sanket" , "om" , "dipak" , "sumit" , "sarvesh"],
    "age" : [ 10, 20,30,45,25,45,65,78]
}

data2 = {
    "EmpId" : [ 10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 ],
    "salary" : [1000 , 2100 , 4000 , 5000 , 2100 , 5400 , 4500 , 6300]
}

# df1 = pd.DataFrame(data1)
# df2 = pd.DataFrame(data2)

# print(df1)
# print(df2)

# # print(pd.merge(df1,df2, on = "EmpId" , how = "left"))

# # print(df1.join(df2))
# print(pd.concat([df1, df2]))

dict = {
    "Fruits" : [ "apple" , "banana" , "mango" , "papaya"],
    "Price" : [100,30,150,50],
    "Quantity" : [ 10 , 50 , 20 , 45 ]
}

df = pd.DataFrame(dict)
print(df)


df2 = df.copy()
print(df2)

df2.loc[0,"Price"] = 100
df2.loc[1,"Price"] = 1001
df2.loc[2,"Price"] = 102
df2.loc[3,"Price"] = 103

print(df2)

print(df.compare(df2,align_axis=1))
print(df.compare(df2,keep_shape=True))