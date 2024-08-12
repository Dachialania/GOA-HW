#1.

n = 5
i = 1

while i <= n:
    print(i)
    i += 1

#2.


numbers = [3, 5, 7, 2, 8]
total = 0
index = 0

while index < len(numbers):
    total += numbers[index]
    index += 1

print("Total sum:", total)


#3.


messages_sent = 0
max_messages = 5

while messages_sent < max_messages:
    print(f"Sending message {messages_sent + 1}")
    messages_sent += 1

print("All messages sent!")


#4.


fruits = ["apple", "banana", "cherry", "date"]
index = 0

while index < len(fruits):
    print(fruits[index])
    index += 1


#5.


n = 10  
a, b = 0, 1
count = 0

while count < n:
    print(a)
    a, b = b, a + b
    count += 1
