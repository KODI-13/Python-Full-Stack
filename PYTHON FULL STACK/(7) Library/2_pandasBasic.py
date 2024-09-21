"""
Pandas --> used to work with data structures/set
           use in data analysist feild for cleaning, fixing, managing and manupulationg data before analysing it
"""
import pandas as p
print(p.__version__)        # attribute/property to check version of it

l = [11,22,33,44]
data = p.Series(l)          # it is a class that creates column (with index number as labels) from data given by us
print(data)
print(data[2])
print("-"*20)

# indes=[] --> we can change indexes according to our choice
l = [11,22,33,44]
# data = p.Series(l,index=[1,2,3,4])     
data = p.Series(l,index=["a","b","c","d"])             
print(data)
print(data['a'])
print("-"*20)

d={"names":["jay","vijay","ajay"],"marks":[67,56,45]}
data = p.Series(d)
print(data)
print("-"*20)

d={"names":["jay","vijay","ajay"],"marks":[67,56,45]}
t = p.DataFrame(d)           # it is a class that creates table (with index number as labels) from data given by us
print(t)
print(t.loc[0])              # loc[index] --> loc is property that gives data of perticuler index
print("-"*20)

d={"names":["jay","vijay","ajay"],"marks":[67,56,45]}
t = p.DataFrame(d,index=['a','b','c'])           # it is a class that creates table (with index number as labels) from data given by us
print(t)
print(t.loc['a'])  
print("-"*20)

"""
function to read from csv and json file
csv file --> Comma seperated values
read_csv() --> read ALL data from file and when you normally print it then it shows first five rows and last five rows
               to print/see all data from file while priniting you have to use to_string() method

read_json() --> read ALL data from file and when you normally print it then it shows first five rows and last five rows
               to print/see all data from file while priniting you have to use to_string() method
"""
#csv
data=p.read_csv("R:/PYTHON FULL STACK/(7) Library/data.csv")
print(data)             
print("-"*150)

data=p.read_csv("R:/PYTHON FULL STACK/(7) Library/data.csv")
print(data.to_string())             
print("-"*150)

#json
data=p.read_json("R:/PYTHON FULL STACK/(7) Library/data.json")
print(data)             
print("-"*150)

data=p.read_json("R:/PYTHON FULL STACK/(7) Library/data.json")
print(data.to_string())             
print("-"*150)

"""
first step to analyse data is to view data
so for viewing data we have two method as follows
head() --> It is method that shows/print first five rowws in the data
           we can pass argument in it to print number of rows we want

tail() --> It is method that shows/print last five rowws in the data
           we can pass argument in it to print number of rows we want
"""
#csv
data=p.read_csv("R:/PYTHON FULL STACK/(7) Library/data.csv")
print(data.head())             
print("-"*150)

data=p.read_csv("R:/PYTHON FULL STACK/(7) Library/data.csv")
print(data.head(10))         # passing argument to print number of rows we want
print("-"*150)

data=p.read_csv("R:/PYTHON FULL STACK/(7) Library/data.csv")
print(data.tail())             
print("-"*150)

data=p.read_csv("R:/PYTHON FULL STACK/(7) Library/data.csv")
print(data.tail(10))         # passing argument to print number of rows we want
print("-"*150)

"""
After viewing data we have to clean it
cleaning refers to removing faulty data, fixing it and managing it
for this we have methods as follows
dropna() --> it deletes data row of the empty cell
fillna() --> it adds details (given by us) at the empty cell in data
drop_duplicates --> it deletes/remove duplicate data in the file
"""
#Dropna() returning new data
data=p.read_csv("R:/PYTHON FULL STACK/(7) Library/data.csv")
data2=data.dropna()
print(data2.to_string())             
print("-"*150)

# # inplace=True  --> it gives permission to change in original data
# data=p.read_csv("R:/PYTHON FULL STACK/(7) Library/data.csv")
# data2=data.dropna(inplace=True)
# print(data2.to_string())             
# print("-"*150)

#fillna() returning new data
data=p.read_csv("R:/PYTHON FULL STACK/(7) Library/data.csv")
data2=data.fillna("OK")
print(data2.to_string())             
print("-"*150)

# # inplace=True  --> it gives permission to change in original data
# data=p.read_csv("R:/PYTHON FULL STACK/(7) Library/data.csv")
# data.fillna("OK",inplace=True)
# print(data2.to_string())             
# print("-"*150)

# drop_duplicates returning new data
data=p.read_csv("R:/PYTHON FULL STACK/(7) Library/data.csv")
data2=data.drop_duplicates()
print(data2.to_string())             
print("-"*150)

# # inplace=True  --> it gives permission to change in original data
# data=p.read_csv("R:/PYTHON FULL STACK/(7) Library/data.csv")
# data.drop_duplicates(inplace=True)
# print(data2.to_string())             
# print("-"*150)
