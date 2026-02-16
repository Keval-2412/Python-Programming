s1 = input("Enter first string:")
s2=input("Enter second string:")
if s1 in s2:
   print("First string is present in second string")
elif s2 in s1:
   print("Second string is present in first string.")
else:
   print("No string is present in the other.")