import string 

def ispangram(s):
    alphabet = set(string.ascii_lowercase)
    return alphabet <= set(s.lower())

print(ispangram("The quick brown fox jumps over the lazy dog"))
