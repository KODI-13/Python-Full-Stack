#biling system

db1={1:"Tea",2:"Misal Pav",3:"Samosa",4:"Vada Pav",5:"Patis",6:"Bhaji Pav",7:"kachori",8:"Dosa"}
db2={1:10,2:30,3:15,4:15,5:20,6:25,7:20,8:25}
i = []
q = []

#name  of hotel
print("-"*100)
print("\t\t\t\t\tHotel Trikut")
print("-"*100) 

while True:                   #What if user takes more than one item ..that's why we used while True to run loop continuosly
    #hotel's menu 
    print("""
    \t\t\t\t       Menu
    \t\t\t\t1.Tea      2.Misal Pav
    \t\t\t\t3.Samosa   4.Vada Pav 
    \t\t\t\t5.Patis    6.Bhaji Pav  
    \t\t\t\t7.Kachori  8.Dosa    
    """) 
    print("-"*100)  

    #input from user what item he/she takes and its quantity
    item = int(input("Enter item number : "))
    quantity = int(input("Enter quantity : ")) 
    i.append(item)
    q.append(quantity) 
    # print(i)
    # print(q)

    ch = input("Anything extra (y/n) : ").lower()           #To break the while True
    if ch == "n":
        print("\n\n\n\t\t\t\t\tRecipt")
        print("-"*85)  
        print("|{:^20}|{:^20}|{:^20}|{:^20}|".format( "Item name" , "Quantity" , "Price" , "Amount"))
        print("-"*85)  
        
        sum = 0
        for j in range(len(i)):                              #To print rows qual to number of items it take's
            print("|{:^20}|{:^20}|{:^20}|{:^20}|".format(db1[i[j]],q[j],db2[i[j]],q[j]*db2[i[j]]))
            print("-"*85)
            sum = sum + q[j]*db2[i[j]]
        gst = sum * 18/100 
        total = sum + gst
        print("Total amount without gst :", sum) 
        print("Total amount with gst :", total)

        print("""
        \t\t\t\t\tThank you
        \t\t\t\t\tVisit again
              """)  

        break
