stack = []
max_size = int(input("Enter size of stack: "))

while True:
    print("\n--- STACK MENU ---")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display Stack")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        if len(stack) == max_size:
            print("Stack Overflow! Cannot push element.")
        else:
            item = input("Enter element to push: ")
            stack.append(item)
            print("Element pushed successfully.")

    elif choice == 2:
        if len(stack) == 0:
            print("Stack Underflow! Nothing to pop.")
        else:
            popped = stack.pop()
            print("Popped element:", popped)

    elif choice == 3:
        if len(stack) == 0:
            print("Stack is empty.")
        else:
            print("Top element:", stack[-1])

    elif choice == 4:
        if len(stack) == 0:
            print("Stack is empty.")
        else:
            print("Stack elements:", stack)

    elif choice == 5:
        print("Exiting program.")
        break

    else:
        print("Invalid choice! Try again.")