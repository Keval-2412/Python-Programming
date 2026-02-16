n = int(input("Enter a number: "))
temp = n
digits = 0
while temp > 0:
    digits += 1
    temp //= 10
temp = n
arm_sum = 0
while temp > 0:
    r = temp % 10
    arm_sum += r ** digits
    temp //= 10
if arm_sum == n:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")