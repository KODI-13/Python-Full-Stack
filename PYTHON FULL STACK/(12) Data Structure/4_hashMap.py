stock_prices = []
with open("r:/PYTHON FULL STACK/(12) Data Structure/data.csv","r") as f:
    for line in f:
        tokens = line.split(',')
        # print(tokens)
        day = tokens[0]
        price = float(tokens[1])
        stock_prices.append([day,price])

print(stock_prices)

for element in stock_prices:
    if element[0] == '9-Mar':
        print(element[1])


print("="*100)
stock_prices = {}
with open("r:/PYTHON FULL STACK/(12) Data Structure/data.csv","r") as f:
    for line in f:
        tokens = line.split(',')
        # print(tokens)
        day = tokens[0]
        price = float(tokens[1])
        stock_prices[day] = price

print(stock_prices)

print(stock_prices['9-Mar'])

#dictionary is implementation of hash table and hash table is internal data structure
#hash function --> for implementation of it there are many ways for e.g. ASCII Table 