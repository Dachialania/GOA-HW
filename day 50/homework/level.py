# 1) შექმენით ფუნქცია, რომელიც პარამეტრად მიიღებს რიცხვების სიას და დააბრუნებს ყველა რიცხვის ნამრავლს. 
# def multiply(listn):
#     result = 1
#     for i in listn:
#         result *= i
#     return result

# listn = [1,2,3,4,5,6]
# print(multiply(listn))

# 2) შექმენით ფუნქცია, რომელიც არგუმენტებად მიიღებს სტრინგს და სიმბოლოს. ფუნქციამ in keyword-ის გამოყენებით უნდა შეამოწმოს 
# არის თუ არა მოცემული სიმბოლო სტრინგში. თუ არის — დააბრუნოს "Found", თუ არა — "Not found".

# def find_string(text,char):
#     if char in text:
#         return 'Found'
#     else:
#         return 'not found'
    
# text = 'Goa is the best'
# char = 'o'
# print(find_string(text,char))

# 3) დაწერეთ ფუნქცია, რომელიც პარამეტრად მიიღებს სტრინგს და დააბრუნებს მის შებრუნებულ ვერსიას.

# def reverse(string):
#     return string[::-1]
    
# string = "Goa is the best"
# print(reverse(string))

# 4) შექმენით ფუნქცია, რომელიც პარამეტრად მიიღებს სიას და დააბრუნებს ახალ სიას, სადაც მხოლოდ უნიკალური ელემენტები იქნება — 
# ანუ თქვენი დავალებაა სია გაფილტროთ duplicate ელემენტებისგან.
# def listn1(listn):
#     return list(set(listn))

# listn = ['banana','banana','hallo','cola']
# print(listn1(listn))    

# 5) დაწერეთ ფუნქცია და გადაეცით ორი არგუმენტი: სია და ელემენტი. ფუნქციამ ჯერ უნდა შეამოწმოს შეიცავს თუ არა სია მოცემულ ელემენტს, თუ შეიცავს ფუნქციამ უნდა დააბრუნოს ამ ელემენტის სიგრძე. თუ არგუმენტად გადაცემული ელემენტი სიაში არ მოიძებნა - მაშინ დააბრუნეთ უშუალოდ სიის სიგრძე.

# def check_element(lst, element):
#     if element in lst:              
#         return len(element)       
#     else:
#         return len(lst) 
    
# lst = ["apple", "banana", "cherry"]
# element = 'banana'
# print(check_element(lst,element))