def count_alpha_digits(s):
    result = {"alphabets" : 0, "digits" : 0}

    for ch in s:
        if ch.isalpha():
            result["alphabets"] += 1
        elif ch.isdigit():
            result["digits"] += 1

        return result
    
print(count_alpha_digits("abc123xyz"))