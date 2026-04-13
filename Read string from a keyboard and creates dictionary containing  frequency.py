a = input("Enter a string: ")
s = a.split()
f = {}
for w in s:
    if w in f:
        f[w] += 1
    else:
        f[w] = 1
max = max(f.values())
print(f)
for k in f:
    if f[k] == max:
        print(k, ":", f[k])
