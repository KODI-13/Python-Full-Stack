#WAp to program to check nword is anagram or not
word1 = input("Enter first word")
word2 = input("Enter second word")

p = len(word1)
q = len(word2) 

r = sorted(word1)
s = sorted(word2)

if p == q and r == s:
    print("it is anagram word " )
else:
    print("it is not anagram word ") 
