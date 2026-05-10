def vowels(a):
        a=a.lower()
        c=len(a.replace(" ",""))
        b="aeiou"
        count1=0
        for i in a:
            if i in b:
                count1+=1  
        print("No of vowels:",count1)
        print ("No of consonants:",c-count1)
a=input("Enter a string:")
vowels(a)