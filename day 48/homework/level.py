# 2) შექმენით manual sum ფუნქცია Python-ში. (manual ნიშნავს გარკვეული ფუნქციის/მეთოდის საკუთარი ხელით შექმნას.)
# ეს ფუნქცია უნდა მუშაობდეს სიებზე, კონკრეტულად: მან უნდა დააბრუნოს სიის ყველა ელემენტის ჯამი.

# def manual_sum(listn):
#     return sum(listn)

# listn = [10,20,30,40,50,60,70]
# print(manual_sum(listn))
    

# 3) დაწერეთ ფუნქცია, რომელიც არგუმენტად მიიღებს მომხმარებლის სახელს, გვარს და ასაკს. ფუნქციამ უნდა დააბრუნოს მომხმარებლის მონაცემები წინადადების სახით. (გამოიყენეთ f string-ი)
# def Guest_information(name,Last_name,age):
#     return f'my name is {name}, my lastname is {Last_name} and i am {age} years old.'

# name = input('Enter your name: ')
# Last_name = input('Enter your lastname: ')
# age = int(input('Enter your age: '))

# print(Guest_information(name,Last_name,age))
    

# 4) შექმენით ფუნქცია - Arithmetic_mean, რომელიც პარამეტრად მიიღებს სიას. ფუნქციამ სიაში არსებული ელემენტების საშუალო არითმეტიკული უნდა დააბრუნოს. 
# (ფუნქცია გათვლილი უნდა იყოს ნებისმიერი რაოდენობის შემცველ სიაზე)

# def Arithmetic_mean(numbers):
#     return sum(numbers) / len(numbers)

# numbers = [10,20,30,40,50,60,70,80,90,100]
# print(Arithmetic_mean(numbers))


# 5) შექმენით ფუნქცია და არგუმენტად გადაეცით String-ი. ფუნქციამ ეგრედწოდებულად უნდა "გაფილტროს" ეს სტრინგი თანხმოვანი ასოებისგან და მხოლოდ დააბრუნოს ის ხმოვანი ასოები, 
# რომლებსაც ეს სტრინგი შეიცავს.

# def alphabet(string):
#     vowels = 'aeiouAEIOU'
#     result = ''
#     for i in string:
#         if i in vowels:
#             result += i
#     return result
    
# string = 'Goal-oriented academy'
# print(alphabet(string))
                
    