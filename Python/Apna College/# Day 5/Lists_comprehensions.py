# Using a loop
sq = []
for i in range(6):
    sq.append(i * i)
print(sq)

# Using list comprehension
square = [i * i for i in range(6)]
print(square)

# Squares of odd numbers only
square = [i * i for i in range(6) if (i % 2) != 0]
print(square)

# Lengths of words
words = ["apple", "banana", "cherry"]
lengths = [len(word) for word in words]
print(lengths)