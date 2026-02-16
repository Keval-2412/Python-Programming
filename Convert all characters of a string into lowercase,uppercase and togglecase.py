def to_lowercase(s):
    result = ""
    for ch in s:
        ascii_val = ord(ch)
        if 65 <= ascii_val <=90:
            result += chr(ascii_val +32)
        else:
            result += ch
    return result
def to_uppercase(s):
    result = ""
    for ch in s:
        ascii_val = ord(ch)
        if 97 <= ascii_val <=122:
            result += chr(ascii_val -32)
        else:
            result += ch
    return result
def toggle_case(s):
    result = ""
    for ch in s:
        ascii_val = ord(ch)
        if 65 <= ascii_val <=90:
            result += chr(ascii_val +32)
        elif 97 <= ascii_val <=122:
            result += chr(ascii_val -32)
        else:
            result += ch
    return result  

string = input("Enter a string: ")
print("Lowercase :", to_lowercase(string))
print("Uppercase :", to_uppercase(string))
print("Toggle Case :", toggle_case(string))      