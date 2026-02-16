import random

odd_list = []
while len(odd_list) < 5:
    num = random.randint(1, 50)
    if num % 2 != 0:
        odd_list.append(num)

print("List of 5 odd integers:", odd_list)

even_list = []
while len(even_list) < 4:
    num = random.randint(1, 50)
    if num % 2 == 0:
        even_list.append(num)

print("List of 4 even integers:", even_list)

odd_list[2] = even_list
print("After replacing 3rd element with even list:", odd_list)

flat_list = []
for item in odd_list:
    if type(item) == list:
        for x in item:
            flat_list.append(x)
    else:
        flat_list.append(item)

print("Flattened list:", flat_list)

flat_list.sort()
print("Sorted list:", flat_list)