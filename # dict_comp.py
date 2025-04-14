
fruits = ["apple", "banana", "cherry"]
word_lengths = {}

# word_lengths = {fruit: len(fruit) for fruit in fruits}
for fruit in fruits:
    word_lengths[fruit] = len(fruit)

print(word_lengths)