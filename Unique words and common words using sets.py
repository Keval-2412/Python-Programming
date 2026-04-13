paragraph = input("Enter a paragraph: ")

words = paragraph.lower().split()
unique_words = set(words)

print("Number of unique words: ", len(unique_words))
print("Unique words: ", unique_words)

sent1 = input("Enter first sentence: ")
sent2 = input("Enter second sentence: ")

set1 = set(sent1.lower().split())
set2 = set(sent2.lower().split())

common_words = set1.intersection(set2)

print("Common words between two sentences: ", common_words)