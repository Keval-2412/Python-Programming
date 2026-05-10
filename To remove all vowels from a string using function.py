def remvow(a):           
           s="aeiouAEIOU"
           for i in a:
              if i in s:
                     a=a.replace(i,"")              
           return a          
a=input("Enter a string:")
print("String without vowels:",remvow(a))