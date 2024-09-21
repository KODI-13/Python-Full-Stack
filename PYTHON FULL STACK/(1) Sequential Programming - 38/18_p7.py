#student__details name age city percentage marks of five subject
#student__details = {1:{"name":deep,"age":21,"city":"pune",marks:{"s1":99,"s2":99.09,"s3":99.99}}}


student_details = {}

for i in range(1,6):
    num = {}
#    roll = int(input("enter your roll number : "))
    name = input("enter your name : ")
    age = int(input("enter your age : "))
    city = input("enter your city : ")

    marks = {} 
    
    maths = eval(input("enter maths marks : "))
    phy = eval(input("enter physics marks : ")) 
    chem = eval(input("enter chemistry marks : ")) 

    marks["mathematics"] = maths
    marks["physics"] = phy
    marks["chemistry"] = chem

    
    num["name"] = name 
    num["age"]  = age 
    num["city"] = city 
    num["marks"] = marks

    student_details[i] = num 

print(student_details) 