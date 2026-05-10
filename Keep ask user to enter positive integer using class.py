while True:
    try:
        num = int(input("Enter a positive integer: "))
        if num > 0:
            print("Valid number entered:", num)
            break
        else:
            print("Error: Number must be positive.")
    except ValueError:
        print("Error: Invalid input. Please enter an integer.")