# Coping one file data to another file (i.e. from "demo.txt" to "demo1.txt")
f1 = open("r:/PYTHON FULL STACK/(4) File Handling - 11/4_demo.txt","r")
d = f1.read()
f2 = open("r:/PYTHON FULL STACK/(4) File Handling - 11/4_demo1.txt","w")
f2.write(d)
f1.close()
f2.close()


