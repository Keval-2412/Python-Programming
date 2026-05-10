def ifdiv(a,b):
    c=[]
    for i in a :
         if i % b == 0 :
             c.append(i)
    print(c)         
n = int(input("Enter number of elements in list: "))
print("Enter elements of list")
a=[int(input()) for i in range (n)]
k=int(input("Enter number to divide with:"))
ifdiv(a,k)