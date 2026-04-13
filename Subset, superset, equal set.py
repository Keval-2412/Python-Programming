set1 = set(map(int, input("Enter elements of first set: ").split()))
set2 = set(map(int, input("Enter elements of second set: ").split()))

if set1.issubset(set2):
    print("Set 1 is a subset of set2 ")
else:
    print("Set 1 is not subset of set 2")

if set2.issuperset(set1):
    print("Set 2 is a superset of set 1")
else:
    print("Set 2 is not superset of set1")

if set1 == set2:
    print("Both sets are equal")
else:
    print("Both sets are not equal")