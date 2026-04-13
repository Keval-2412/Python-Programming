def count_lower_upper(s):
    result = {"uppercase": 0, "lowercase": 0}

    for ch in s:
        if ch.isupper():
            result["uppercase"] += 1
        elif ch.islower():
            result["lowercase"] += 1

        return result

print(count_lower_upper("Hello World"))