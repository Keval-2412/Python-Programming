s = input("Enter a string: ")
print("First character: ", s[0])
print("Last character :", s[len(s) - 1])

if len(s) % 2 != 0:
    mid = len(s) // 2
    print("Middle character: ", s[mid])
else:
    print("Middle character : Not applicable (length is even)")