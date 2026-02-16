strings = ["python", "java", "c", "html", "sql"]

i = 0
while i < len(strings):
    strings[i] = strings[i].upper()
    i += 1

print("List after converting to uppercase:")
print(strings)