def frequency(s):
    words = s.split()
    freq = {}

    for word in words:
        freq[word] = freq.get(word, 0) + 1

        return dict(sorted(freq.items()))
    
print(frequency("apple banana apple orange banana apple"))