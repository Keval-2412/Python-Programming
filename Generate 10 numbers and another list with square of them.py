import random

numbers = random.sample(range(-15,16), 10)

squares = [x**2 for x in numbers]

print("Random Numbers: ", numbers)
print("Squares: ", squares)