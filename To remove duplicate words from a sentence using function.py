def rep(n):
    n=n.lower()
    a=n.split()
    a=list(set(a))
    print(a)
        
a=input("Enter a paragraph:")
rep(a)