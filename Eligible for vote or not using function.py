# Python program to check voting eligibility using function

def check_vote(age):
    if age >= 18:
        print("Eligible to vote")
    else:
        print("Not eligible to vote")

# Input from user
age = int(input("Enter your age: "))

# Function call
check_vote(age)