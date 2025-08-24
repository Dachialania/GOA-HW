# 1) შექმენით ფუნქცია და გადაეცით რიცხვების სია არგუმენტად. ფუნქციის მიზანი იქნება, რომ სიიდან დააბრუნოს მხოლოდ უარყოფითი რიცხვები.
# def numbers_list(numbers):
#     negative_numbers = []
#     for i in numbers:
#         if i < 0:
#             negative_numbers.append(i)
#     return negative_numbers

# numbers = [1,2,3,4,5,-1,-2,-3,10]
# print(numbers_list(numbers))                

# 2) წინა დავალების ანალოგიურად შექმენით ფუნქცია და გადაეცით რიცხვების სია არგუმენტად. ამ შემთხვევაში ფუნქციის მიზანი იქნება, რომ სიიდან დააბრუნოს მხოლოდ დადებითი რიცხვები.
# def numbers_list(numbers):
#     positive_numbers = []
#     for i in numbers:
#         if i > 0:
#             positive_numbers.append(i)
#     return positive_numbers

# numbers = [1,2,3,4,5,-1,-2,-3,10]
# print(numbers_list(numbers))
# 3) შექმენით ფუნქცია და მას პარამეტრად  გადაეცით სამი რიცხვი. ფუნქციამ უნდა დააბრუნოს პირველი რიცხვი აყანილი მეორე რიცხვის ხარისში და გამრავლებული მესამე რიცხვზე.

def triple_number(num1,num2,num3):
    return (num1 ** num2) * num3

num1 = 2
num2 = 3
num3 = 5

print(triple_number(num1,num2,num3))