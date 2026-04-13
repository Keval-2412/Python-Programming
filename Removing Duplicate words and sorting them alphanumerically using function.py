def convert(s):
    words = s.split()
    unique_words = sorted(set(words))
    return " ".join(unique_words)

print(convert("hello world hello python world"))