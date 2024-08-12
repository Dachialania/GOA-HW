#1.
numbers = [1, 4, 5, 6, 9, 3, 7, 2, 8]

greater_or_equal_five = []
less_than_five = []

for number in numbers:
    if number >= 5:
        greater_or_equal_five.append(number)
    else:
        less_than_five.append(number)

print("Numbers greater than or equal to 5:", greater_or_equal_five)
print("Numbers less than 5:", less_than_five)


#2.
numbers = [2, 4, 6, 8, 10]
multiplier = 3
results = []

for number in numbers:
    if number % 2 == 0:  # შემოწმება, რომ ნომერი იყოს წყვილი
        results.append(number * multiplier)

print("Multiplied numbers:", results)


#3.
words = ["apple", "banana", "cherry", "kiwi", "mango"]
long_words = []
short_words = []

for word in words:
    if len(word) >= 4:
        long_words.append(word)
    else:
        short_words.append(word)

print("Words with 4 or more letters:", long_words)
print("Words with less than 4 letters:", short_words)
