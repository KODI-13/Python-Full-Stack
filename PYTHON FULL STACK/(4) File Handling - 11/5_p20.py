# To count number of lines , words and character from a file
f1 = open("r:/PYTHON FULL STACK/(4) File Handling - 11/4_demo.txt","r")
count_line = 0
count_word = 0
count_character = 0
for i in f1:
    # print(i)
    count_line = count_line + 1
    d = i.split()
    # print(d)
    count_word = count_word + len(d)
    k = sorted(i)
    # print(k)
    for j in k:
        if j == " " or j == "\n":
            continue
        else:
            count_character = count_character + 1

print("\ncount_line : ",count_line)

print("\ncount_word : ",count_word)

print("\ncount_character: ",count_character)

f1.close()