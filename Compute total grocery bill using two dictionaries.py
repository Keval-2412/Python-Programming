prices = {
    'rice' : 50,
    'wheat' : 40,
    'milk' : 30
}

quantity = {
    'rice' : 2,
    'wheat' : 3,
    'milk' : 1
}

total = 0

for item in prices:
   total += prices[item] * quantity.get(item, 0)

print("Total bill:", total)