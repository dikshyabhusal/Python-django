input_word = input("Enter a word: ")
words = input_word.split()

word_lengths = {word: len(word) for word in words}

print("Word Lengths:", word_lengths)
