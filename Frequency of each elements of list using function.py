#Python program to find frequency of elements in a list

def frequency(lst):
    freq = {}
    
    for item in lst:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
            
    return freq

numbers = list(map(int, input("Enter numbers by space between them: ").split()))

print(frequency(numbers))