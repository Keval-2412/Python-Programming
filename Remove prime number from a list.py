def prime(i):
        if i>1:
         for j in range(2,i):
            if i%j==0:
                return True   
            else:
                return False    
        elif i==1:
             return True
print("Enter a list:")    
a=[int(input()) for i in range (5)]
b=list(filter(prime,a))
print(b)