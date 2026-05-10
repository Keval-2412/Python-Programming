def com(a,b):
    c=[]
    for i in a:
        if i in b:
            c.append(i)
    return c       
print("Enter elements of list A:")
a=[int(input()) for i in range (5)]
print("Enter elements of list B:")
b=[int(input()) for i in range (5)]
print("List of common elements of A & B:",com(a,b))