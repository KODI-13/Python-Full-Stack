"""
volitile memory --> temporary memory == e.g. RAM is random access memory use to store data temporary
non-volitile memory --> permanent memory

so there are two ways to store data permanently
1) File Handling ---> used when we have to work on small data, small application project
2) Database (sql) ---> used for big data, big application project

file --> file is used to store data permanenetly
         It is non volatile memory (i.e. data is store inside non volitile memory)
         files are named memory location to store information and data ; and we can access data whenever we want
         Types of files --> 1) Text file --> use to store sting data type only....extention is .txt
         9]
                                                                               e.g.  .txt
                                                  .json

                            2) Binary file --> use to store bytes data
                                            e.g.  .jpg
                                                  .mp3
                                                  .mp4
                                                  .png

file handling -- > The process of opening files and performing some operation on it and closing the file is called as file handling
                   main term --> open file
                                 opr.
                                 close file
for opening file we use
open() = It is a function to open file   
         It returns an object which we have to store in the variable                                                
         sytnax: 
                  f = open("File_name","mode",Buffering,encoding,error)          f is called as file handler

         File_name = First attribute  ... The name of file on which we have to perform opertations                               ... written inside double coat
         Mode      = Second attribute ... The purpose to oopen the file (*NOTE = purpose means read from file or write in file )  ... written inside double coat
         buffernig = Third attribute  ... We set buffer value in the buffering ... It's value is positive integer value(not negative / nor in point) use to set buffer size for a file
                                                                                   in text file/mode buffer size SHOULD be 1 or more than 1
                                                                                   in binary mode buffer size CAN BE 0 
                                                                                   DEFAULT SIZE IS 4095 TO 8192 BYTES

         encoding  = Fourth attribute ... Encoding type use to encode and decode file ... It is only used in text mode/file (*NOTE = Not used in binary mode/ file)
                                                                                          default value depends on operating system
                                                                                          FOE WINF\DOWS cp1252

         error     = Fifth attribute  ... Represnts how to handle encoding and decoding error ... It is only used in text mode/file  (*NOTE = Not used in binary mode/ file)
                                                                                                  have some standerd value -- > strict = check the error stictly
                                                                                                                                ignore = ignore the error
                                                                                                                                replace 

(*NOTE  buffernig 
                 for e.g you have python file and and have another file with 10gb data
                 you want to transfer/load 10gb data to your python file
                 but you can't directly transfer/process these data
                 in that case the main memory of computer has buffer memory 
                 so we set buffer value of 10gb data in the buffer memory
                 hence that the data is divided into n number of chunks. 
                 SO THE VALUE OF 1 CHUNK IS EQUAL TO THE BUFFER VALUE SET BY US
                 and these chunks loads into python file)

for closing file we use
close()  = It is a method to close file   
           sytnax: 
                  File_handler.close()          

           closing files means the file object is deleted from memory and file is not accessable until we opens it agains
           what if we didn't close the file -- > then the garbage collector automatically deletes the file after the entire program is executed
           but it is good practice to close the file by yourself otherwise data might be losse/corrupt and the memory wastage can be occured

Attributes 
name   = It is a variable/attrribute/proprty which returns the name of file                                                   syntax: File_Handler.name
mode   = It is a variable/attrribute/proprty which returns the mode for which file is opened                                  syntax: File_Handler.mode
closed = It is a variable/attrribute/proprty which check if file is open or not and return the output in boolean format       syntax: File_Handler.closed 

Metods
readable = It is a method which check if open file is readable or not and return the output in boolean format                 syntax: File_Handler.readable()
Writable = It is a method which check if open file is writable or not and return the output in boolean format                 syntax: File_Handler.readable()

Three ways to close file
1) Normal way -->  syntax: 
                           f = open("program.txt","w")
                           \
                              performing some operations
                           \
                           f.close()

                   but if there is an error while performing some operations..then the code after error will not get executed (beacuse python is interpreted language) and data may get corrupted or memory wastge may occured

2) Using exception handling
   Try and except  --> syntax:
                              try:
                                    \
                                       full program written here 
                                       (*NOTE = The program which may give error is written inside try Block)
                                       but if there is no error occur inside try block then except block will not get executed and finally block will always executed
                                    \
                              except:
                                    \
                                      error handling block
                                      (*NOTE = The program to handle error After it errors)
                                      but if there is an error occur inside try block then except block will get executed and finally block will always executed

                                    \
                              finally:
                                    \
                                     it always get executed
                                    \

3) With statement -->  syntax: 
                              with open("File_name","mode") as File_handler:
                                    \
                                       performing some operations
                                    \

                        The file is closed automatically
"""


f = open("r:/PYTHON FULL STACK/(4) File Handling - 11/1_fh.txt","w")
age = input("Enter age : ")
f.write(age)
f.close()

f = open("r:/PYTHON FULL STACK/(4) File Handling - 11/1_fh.txt","r")
age=f.read()
print(age)
f.close()

f = open("r:/PYTHON FULL STACK/(4) File Handling - 11/1_fh.txt","r")
if f:                                           # To check whether file is opened successfully or not
    print("Open successfully...")
f.close()

f = open("r:/PYTHON FULL STACK/(4) File Handling - 11/1_fh.txt","w")
f.write("Deepak")
f.close()
# f.write("siddhi")

f = open("r:/PYTHON FULL STACK/(4) File Handling - 11/1_fh.txt","w")
print(f.name)
print(f.mode)
print(f.closed)
print(f.readable())
print(f.writable())
f.close()
print(f.closed)

# If error not occured 
try:
    f = open("r:/PYTHON FULL STACK/(4) File Handling - 11/1_fh.txt","r")
    data=f.read()
    print(f.closed)
    print(data)
except:
    print("Something went wrong")
finally:
    f.close()
    print(f.closed)

# # If error occured 
# try:
#     f = open("r:/PYTHON FULL STACK/(4) File Handling - 11/1_fh.txt","r")
#     data=f.read()
#     print(f.closed)
#     print(data1)
# except:
#     print("Something went wrong")
# finally:
#     f.close()
#     print(f.closed)


with open("r:/PYTHON FULL STACK/(4) File Handling - 11/1_fh.txt","r") as f:
    data=f.read()
    print(data)
    print(f.closed)
print(f.closed)