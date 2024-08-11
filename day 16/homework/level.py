numbers = list(range(1, 21))
sum_odd = 0

for number in numbers:
    if number % 2 != 0:
        sum_odd = sum_odd + number

print("კენტი რიცხვების ჯამი 1-დან 20-მდე:", sum_odd)    


 words = ["apple","grey","nigga","fig","etc"]   
a_words = []
for word in words:
    if "a" in word:
        a_words.append(word)
    else:
        pass
print(f"words that has a in it are: {a_words}") 



numbers = [-11,15,-4,-5,5,6,2,-10]   
positive_numbs = []


for number in numbers:
    if number > 0:
        positive_numbs.append(number)
    else:
        pass
print(f"positive numbers in list are: {positive_numbs}")    