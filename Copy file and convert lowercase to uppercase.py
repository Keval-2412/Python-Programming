with open("source.txt", "r") as f1:
    content = f1.read()

content = content.upper()

with open("target.txt", "w") as f2:
    f2.write(content)

print("File copied with uppercase conversion.")