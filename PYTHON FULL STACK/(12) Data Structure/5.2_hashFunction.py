
"""
1) nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
What was the average temperature in first week of Jan
What was the maximum temperature in first 10 days of Jan
Figure out data structure that is best for this problem
"""
report = []
with open("r:/PYTHON FULL STACK/(12) Data Structure/nyc_weather.csv","r") as f:
    count = 0
    for line in f:
        token = line.split(',')
        # print(token)
        if count != 0:
            date = token[0]
            temprature = float(token[1])
            report.append(temprature)

        count += 1

print(report)

# What was the average temperature in first week of Jan
avg = sum(report[0:7])/len(report[0:7])
print(avg)

# What was the maximum temperature in first 10 days of Jan
m = max(report[0:10])
print(m)


"""
2) nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
What was the temperature on Jan 9?
What was the temperature on Jan 4?
Figure out data structure that is best for this problem
"""
report = {}
with open("r:/PYTHON FULL STACK/(12) Data Structure/nyc_weather.csv","r") as f:
    count = 0
    for line in f:
        token = line.split(',')
        # print(token)
        if count != 0:
            date = token[0]
            temprature = float(token[1])
            report[date] = temprature

        count += 1

# What was the temperature on Jan 9?
print(report["Jan 9"])
# What was the temperature on Jan 4?
print(report["Jan 4"])

"""
3) poem.txt Contains famous poem "Road not taken" by poet Robert Frost. You have to read this file in python and print every word and its count as show below. Think about the best data structure that you can use to solve this problem and figure out why you selected that specific data structure.
"""

poem = []
line_count = 0
word_count = 0
with open("r:/PYTHON FULL STACK/(12) Data Structure/poem.txt","r") as f:
    for line in f:
        poem.append(line)
        line_count += 1
        d = line.split()
        word_count += len(d)
# print(poem)
print(line_count)
print(word_count)

word_count = {}
with open("r:/PYTHON FULL STACK/(12) Data Structure/poem.txt","r") as f:
    for line in f:
        tokens = line.split(" ")
        # print(tokens)
        for token in tokens:
            token=token.replace('\n','')
            # print(token)
            if token in word_count:
                word_count[token]+=1
            else:
                word_count[token]=1
print(word_count)