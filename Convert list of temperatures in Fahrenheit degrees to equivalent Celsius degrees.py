n = int(input("Enter number of temperatures you want to convert:"))
fahrenheit = []
celsius = []

i = 0
while i < n:
    temp = float(input("Enter temperature in Fahrenheit:"))
    fahrenheit.append(temp)
    i += 1

i = 0
while i < len(fahrenheit):
    c = (5 / 9) * (fahrenheit[i] - 32)
    celsius.append(c)
    i += 1

print("\nTemperatures in Fahrenheit:", fahrenheit)
print("Temperatures in Celsius:", celsius)