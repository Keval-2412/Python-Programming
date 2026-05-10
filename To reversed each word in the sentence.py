# Function to reverse each word in a sentence
def reverse_words(sentence):
    words = sentence.split()   # Split sentence into words
    reversed_sentence = []

    for word in words:
        reversed_sentence.append(word[::-1])   # Reverse each word

    return " ".join(reversed_sentence)   # Join words into sentence
# Accept sentence from user
sentence = input("Enter a sentence: ")

# Call function and display result
result = reverse_words(sentence)

print("Sentence with each word reversed:", result)