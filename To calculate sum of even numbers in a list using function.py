def sum_even(a):
    sum=0
    for i in a:
        if i%2==0:
            sum=sum+i
    return sum  
print("Enter elements of list A:")
a=[int(input()) for i in range (5)]     
print("Sum of even elements:",sum_even(a)) 