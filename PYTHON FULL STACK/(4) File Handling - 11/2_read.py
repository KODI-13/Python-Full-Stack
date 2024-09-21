"""
Reading data --> Methods 
                  a) read()      ... read all data                                                          syntax: file_handler.read()
                                     we can give no of character to read                                    syntax: file_handler.read(size)

                  b) readline()  ... read one line                                                          syntax: file_handler.readline()
                                     we can give no of character to read but this read only in one line     syntax: file_handler.readline(size)
                                                                    
                  b) readlines() ... return a list of lines                                                 syntax: file_handler.read()

Method
tell() - this method used to find(i.e. return) the current position of pointer from beginning of file       syntax: file_handler.tell()
         (*NOTE = cursor / pointer poistion is starts from 0 and it will also count the position of \n )
seek() - this method is used to change the position of pointer                                              syntax: file_handler.seeek(position)
"""
# read() method
f = open("R:/PYTHON FULL STACK/(4) File Handling - 11/2_read.txt","r")
if f:
    print("done")
data = f.read()
print(data)
f.close()
print("-------------\n\n-------------")

f = open("R:/PYTHON FULL STACK/(4) File Handling - 11/2_read.txt","r")
data = f.read(2)
print(data)
f.close()
print("-------------\n\n-------------")


f = open("R:/PYTHON FULL STACK/(4) File Handling - 11/2_read.txt","r")
data = f.read(10)
print(data)
f.close()
print("-------------\n\n-------------")


f = open("R:/PYTHON FULL STACK/(4) File Handling - 11/2_read.txt","r")
data = f.read(10)
data2 = f.read(3)
print(data)
print(data2)
f.close()
print("-------------\n\n-------------")


f = open("R:/PYTHON FULL STACK/(4) File Handling - 11/2_read.txt","r")
data = f.read(10)
data2 = f.read(3)
print(data,end="")
print(data2)
f.close()
print("-------------\n\n-------------")

# readline() method
f = open("R:/PYTHON FULL STACK/(4) File Handling - 11/2_read.txt","r")
data = f.readline()
print(data)
f.close()
print("-------------\n\n-------------")


f = open("R:/PYTHON FULL STACK/(4) File Handling - 11/2_read.txt","r")
data = f.readline()
data2 = f.readline()
print(data)
print(data2)
f.close()
print("-------------\n\n-------------")

f = open("R:/PYTHON FULL STACK/(4) File Handling - 11/2_read.txt","r")
data = f.readline()
data2 = f.readline()
print(data,end ="")
print(data2,end="")
f.close()
print("-------------\n\n-------------")

f = open("R:/PYTHON FULL STACK/(4) File Handling - 11/2_read.txt","r")
data = f.readline(1)
print(data)
f.close()
print("-------------\n\n-------------")


f = open("R:/PYTHON FULL STACK/(4) File Handling - 11/2_read.txt","r")
data = f.readline(10)
print(data)
f.close()
print("-------------\n\n-------------")

f = open("R:/PYTHON FULL STACK/(4) File Handling - 11/2_read.txt","r")
data = f.readline(1)
data2 = f.readline(3)
print(data)
print(data2)
f.close()
print("-------------\n\n-------------")

# readlines() method
f = open("R:/PYTHON FULL STACK/(4) File Handling - 11/2_read.txt","r")
data = f.readlines()
print(data)
for i in data:
    print(i)
f.close()
print("-------------\n\n-------------")

# Method -->
# tell()
f = open("R:/PYTHON FULL STACK/(4) File Handling - 11/2_read.txt","r")
print("position:", f.tell())
data = f.read(3)
print(data)
print("position:", f.tell())
f.close()
print("-------------\n\n-------------")

# seek()
f = open("R:/PYTHON FULL STACK/(4) File Handling - 11/2_read.txt","r")
print("positomn:", f.tell())
data = f.read(5)
print(data)
f.seek(0)
print("positomn:", f.tell())
data1 = f.read(3)
print(data1)
f.close()
print("-------------\n\n-------------")

