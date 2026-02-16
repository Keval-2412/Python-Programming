queue = []
max_size = int(input("Enter size of queue: "))

while True:
    print("\n--- QUEUE MENU ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display Queue")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        if len(queue) == max_size:
            print("Queue Overflow! Cannot insert.")
        else:
            item = input("Enter element to insert: ")
            queue.append(item)
            print("Element inserted successfully.")

    elif choice == 2:
        if len(queue) == 0:
            print("Queue Underflow! Nothing to delete.")
        else:
            removed = queue.pop(0)
            print("Deleted element:", removed)

    elif choice == 3:
        if len(queue) == 0:
            print("Queue is empty.")
        else:
            print("Queue elements:", queue)

    elif choice == 4:
        print("Exiting program.")
        break

    else:
        print("Invalid choice! Try again.")