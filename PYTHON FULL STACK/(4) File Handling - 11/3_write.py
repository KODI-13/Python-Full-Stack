"""
Writing in file --> mode --> "w" , "a" , "x"
"w" mode--> it open a file to write only
            it overrides data in file
            if a file dosen't exist it creates new file
            the file pointer exist at the beginnig of the file
            it has two methods to write in w mode
                                1) write() --> use to write string type of data in file
                                2) writelines() --> use to write a group of lines of string data-type into a file represented by a file oject
                                                    group of lines store in a collective data type (*NOTE = i.e. it takes a sequence like list, tuple, set)

append mode /"a" mode --> it does not override the file
                          it has same methods like "w" mode i.e. write() and writelines()

"x" mode --> always add the data to new file
             does not write on existing file .. if existing file with current name occur then it shows error

"""
# "w" mode
# write()
f =  open("r:/PYTHON FULL STACK/(4) File Handling - 11/3_write.txt","w")    
# d = f.read()                                                            # it open a file to write only
f.write("jhatu")
f.close()

f =  open("r:/PYTHON FULL STACK/(4) File Handling - 11/3_write.txt","w")     # it overrides above data in file
f.write("tondaat ghe maza")
f.close()

f =  open("r:/PYTHON FULL STACK/(4) File Handling - 11/3_write1.txt","w")     # if a file dosen't exist it creates new file
f.write("lavdya")
f.close()

# writelines()
f =  open("r:/PYTHON FULL STACK/(4) File Handling - 11/3_write.txt","w")      # if a file dosen't exist it creates new file
f.writelines(["baghots\n","kay\n","mujara\n","kar"])
f.close()

# append mode /"a" mode 
f =  open("r:/PYTHON FULL STACK/(4) File Handling - 11/3_write.txt","a")
f.write("\njhatu")
f.close()

# "x" mode
f =  open("r:/PYTHON FULL STACK/(4) File Handling - 11/3_write.txt","x")       # does not write on existing file
f.write("jhatu")
f.close()

"""
r --> read only
w --> write only
r+ --> read and write
w+ --> write and read  ..... is not working
"""

f =  open("r:/PYTHON FULL STACK/(4) File Handling - 11/3_write.txt","r+")
print(f.read())
data = f.write("jhatu lavdya")
f.close()

f =  open("r:/PYTHON FULL STACK/(4) File Handling - 11/3_write.txt","w+")
f.write("jhatu")
data = f.read()
print(data)
f.close()