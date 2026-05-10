with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2:
    lines1 = f1.readlines()
    lines2 = f2.readlines()

merged = []

max_len = max(len(lines1), len(lines2))

for i in range(max_len):
    if i < len(lines1):
        merged.append(lines1[i])
    if i < len(lines2):
        merged.append(lines2[i])

with open("merged.txt", "w") as f:
    f.writelines(merged)

print("Files merged successfully.")