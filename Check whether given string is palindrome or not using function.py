lst = ['madam', 'Python', 'malayalam', 12321]

print("Palindromes: ")
for item in lst:
    s = str(item)
    if s == s[::-1]:
        print(item)