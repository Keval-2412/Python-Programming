# Python program to calculate total and average
def sum_avg(m1, m2, m3, m4, m5):
    total = m1 + m2 + m3 + m4 + m5
    avg = total / 5
    return total, avg
# Input marks
a = int(input("Enter marks of subject 1: "))
b = int(input("Enter marks of subject 2: "))
c = int(input("Enter marks of subject 3: "))
d = int(input("Enter marks of subject 4: "))
e = int(input("Enter marks of subject 5: "))

total, average = sum_avg(a, b, c, d, e)

print("Total =", total)
print("Average =", average)