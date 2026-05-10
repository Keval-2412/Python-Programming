def fre(n):
    c={}
    n = n.lower()
    a = n.split()
    for i in a :
        count=0
        for j in a:
         if j==i:
            count += 1
            c[i] = count
    print(c)    
a=input("Enter a paragraph:")
fre(a)