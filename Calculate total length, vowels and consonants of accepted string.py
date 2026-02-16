s = input("Enter a string: ")
length = 0
vowels = 0
consonants = 0
i = 0
while i < len(s):
    ch = s[i]
    length += 1

    if('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
        if ch in 'AEIOUaeiou':
            vowels += 1
        else:
            consonants += 1
    i += 1
print("Total length :", length)
print("Number of vowels :", vowels)
print("Number of consonants :", consonants)