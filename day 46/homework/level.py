# 2) შექმენით ფუნქცია check_age, რომელიც არგუმენტად მიიღებს მომხმარებლის ასაკს.
# თუ მომხმარებლის ასაკი მეტი ან ტოლი იქნება 18-ზე, ტერმინალში დაიბეჭდოს "Access Granted", წინააღმდეგ შემთხვევაში – "Access Denied".
# def check_age(age):
#     if age >= 18:
#         return 'Access Granted'
#     else:
#         return 'Access Denied'
    
# age = int(input('how old are you? '))
# print(check_age(age))

# 3) შექმენით ფუნქცია print_names, რომელიც მიიღებს სახელების სიას და ტერმინალში თითოეული მათგანს ცალ-ცალკე ხაზზე დაბეჭდავს.
# def print_names(names_list):
#     for i in names_list:
#         print(i) 
    
# names_list = ['dachi','dito','luka']
# name = print_names(names_list)
# print(name)
# 4) დაწერეთ ფუნქცია სახელწოდებით odd_or_even. ფუნქციამ უნდა დააბრუნოს Even თუ არგუმენტად გადაცემული რიცხვი ლუწია, ხოლო Odd - თუ კენტი.
# def odd_or_even(num):
#     if num % 2 == 0:
#         return 'Even'
#     else:
#         return 'Odd'
    
# num = int(input('Enter a number: '))
# print(odd_or_even(num))
        

# 5) შექმენით ფუნქცია student_grade, რომელიც იღებს მოსწავლის ქულას (0-დან 100-მდე) და ტერმინალში დაბეჭდავს შემდეგ ქულებს:

#     • 90-100: - A

#     • 70-89: - B

#     • 50-69: - C

#     • 0-49: - F

# def student_grade(score):
#     if 90 <= score <= 100:
#         return 'A'
#     elif 70 <= score <= 89:
#         return 'B'
#     elif 50 <= score <= 69:
#         return 'C'
#     elif 0 <= score <= 49:
#         return 'F'

# score = int(input('Enter your score: '))
# print(student_grade(score))
        
        