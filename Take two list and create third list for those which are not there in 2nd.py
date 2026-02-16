list1 = [1,2,3,4,5,6]
list2 = [2,4,6,8]

list3 = [x for x in list1 if x not in list2]

print("First list: ", list1)
print("Second list: ", list2)
print("Third list (NOT IN SECOND): ", list3)