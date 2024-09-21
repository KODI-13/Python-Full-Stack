#D*Mart biling system

db1={1:"Suger", 2:"rice", 3: "Tomato", 4 : "Potato" ,5:"Flour", 6:"Mixed nuts" , 7:"Oats" , 8: "Pinut butter",9:"Jeera",10:"Badam"}
    
db2={1:40,2:70,3:100,4:40,5:50,6:80,7:200,8:350,9:40,10:500}
i = []
q = []
d = []

#name  of D*mart
print("-"*100)
print("\t\t\t\t\t\tD*Mart")
print("-"*100) 

while True:                   #What if user takes more than one item ..that's why we used while True to run loop continuosly
    #hotel's menu 
    print("""
        \t\t\t\t       Menu
        \t\t\t\t1.Sugar    2.Rice
        \t\t\t\t3.Tomato   4.Potato
        \t\t\t\t5.Flour    6.Mixed nuts
        \t\t\t\t7.Oats     8.Pinut butter   
        \t\t\t\t9.Jeera    10.badam
        """)
    print("-"*100)  

    #input from user what item he/she takes and its quantity
    item = int(input("Enter item number : "))
    quantity = int(input("Enter quantity : ")) 
    discount = int(input("Enter discount : "))
    i.append(item)
    q.append(quantity) 
    d.append(discount)
    # print(i)
    # print(q)

    ch = input("Anything extra (y/n) : ").lower()           #To break the while True
    if ch == "n":
        print("\n\n\n\t\t\t\t\tRecipt")
        print("-"*106)  
        print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format( "Item name" , "Quantity" , "Price" , "Discount" , "Amount"))
        print("-"*106)  
        
        sum = 0
        total = 0
        for j in range(len(i)):                             #To print rows qual to number of items it take's
            print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format(db1[i[j]],q[j],db2[i[j]],d[j],q[j]*db2[i[j]]))
            print("-"*106)
            sum = sum + q[j]*db2[i[j]]
            #To calculate sepearete discount prize of each item from discount percentage
            dis_prize = q[j]*db2[i[j]] * d[j]/100 
            #It gives amount after discount
            z = q[j]*db2[i[j]] - dis_prize 
            #It do summation of all the amount after discount
            total = total + z 
        print("Total amount without discount :", sum) 
        print("Total amount with discount :", total)

        print("""
        \t\t\t\t\tThank you
        \t\t\t\t\tVisit again
              """)  

        break