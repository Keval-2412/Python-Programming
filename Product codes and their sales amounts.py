import operator 
a ={'101' : 230 , '107' : 120}
b = {'101' : 230, '108' : 120}

for k in b:
    b[k] = a[k] + b[k]

for k in a:
    if k not in b:
        b[k] = a[k]

max = max (b.values())
for k, v in b.items():
    if v == max:
        print(k, ":" , v)
d = sorted(b.items(), key = operator.itemgetter(1), reverse = True)
print(d)