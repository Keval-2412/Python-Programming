#Python program to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

celsius = float(input("Enter Celsius: "))
print(celsius_to_fahrenheit(celsius))