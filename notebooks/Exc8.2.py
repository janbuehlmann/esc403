def count_words(words, min_word_length):
    counter = 0

    for word in words:
      if len(word) >= min_word_length:
          counter += 1
    return counter

names = ["Anna", "Peter", "John", "Andreas"]
count_words(names, 5)

print(count_words(names, 5))

