def create_list(list1, list2):
    result = list(set(list1).intersection(set(list2)))
    return result

list1 = list(map(int, input("Enter the first list of numbers (comma separated): ").split(',')))
list2 = list(map(int, input("Enter the second list of numbers (comma separated): ").split(',')))

intersection_list = create_list(list1,list2)
print("Intersection of two lists: ", intersection_list)