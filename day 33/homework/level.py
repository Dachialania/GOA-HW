# 2) მოცემულია სია:

# nums = [10, 20, 30, 40, 50, 60]

# დაბეჭდეთ: სიის პირველი ელემენტი, ბოლო ელემენტი და საბოლოოდ რიცხვები 30, 40.
# nums = [10, 20, 30, 40, 50, 60]
# print(nums[0])
# print(nums[-1])
# print(nums[2:4])
# 3) შექმენით ცვლადი word = "Programming" და დაბეჭდეთ ცვლადის:

#     • პირველი ასო
# word = "Programming"
# print(word[:1])

#     • ბოლო ასო
# word = "Programming"
# print(word[-1])
#     • "gram" slicing-ით
# word = "Programming"
# print(word[3:7])

#     • სიტყვა შებრუნებულად
# word = "Programming"
# print(word[::-1])

# 4) მომხმარებელს შემოატანინე წინადადება input-ის გამოყენებით, ტერმინალში კი დაბეჭდე ჯერ ამ წინადადების პირველი ასოს და ბოლო ასოს ნაერთი. ბოლოს ეს მთლიანი 
# წინადადება დაბეჭდეთ ტერმინალში უკუღმა.
# username = input("Enter your username: ")
# username1 = username[0] + username[-1]
# print(username1)
# print(username[::-1])
# 5) შექმენით სია [1, 2, 3, 4, 5].
# მომხმარებელს შეეკითხეთ ჯერ რომელ ინდექსზე სურს ელემენტის ჩანაცვლება, შემდეგ თუ რა ელემენტით უნდა ამ კონკრეტულ ინდექსზე მყოფი რიცხვის ჩანაცვლება და 
# ამის მიხედვით შეცვალეთ სია. სიის თავდაპირველი და ბოლო სახეები გამოიტანეთ ტერმინალში.
# numbers = [1, 2, 3, 4, 5]
# Guest = int(input("Which index do you want to change? "))
# Guest1 = input("What element would you like to be immersed in?")
# print(numbers)
# numbers[Guest] = Guest1 
# print(numbers)

# 6) შექმენით სია და შეამოწმეთ, არის თუ არა ის სიმეტრიული (მაგ: [1, 2, 3, 2, 1]).

# # Output: "Symmetric" ან "Not symmetric"

# hint: დაგჭირდებათ Slicing.
# numbers = [1, 2, 3, 2, 1]
# if numbers == numbers[::-1]:
#     print("Symmetric")
# else:
#     print("Not symmetric")
# 7) შექმენი რიცხვების სია, სადაც დაამატებთ 8 რიცხვს. ცალკეულ ცვლადებში შეინახეთ ამ სიის საშუალო არითმეტიკული და სიის რიცხვების ჯამი. 
# ბოლოს f string-ის გამოყენებით გამოიტანეთ მსგავსი წინადადებები:
 

# The aritchmetic mean of this list is: ...
# The sum of all numbers in this list is: ...
 
number = [1,2,3,4,5,6,7,8]
sum_of_number = 0
count = 0
for i in number:
    sum_of_number += i
    count += 1 
    result = sum_of_number / count
    print(f'The aritchmetic mean of this list is: {result} ')
    print(f'The sum of all numbers in this list is: {sum_of_number}')
        
    