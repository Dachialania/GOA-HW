# 1) მომხმარებელს შემოატანინეთ მთელი რიცხვი და დაწერეთ პროგრამა, რომელიც ამოწმებს:

# • თუ რიცხვი დადებითია, დაბეჭდოს: "the number is positive"
# • თუ უარყოფითია, დაბეჭდოს: "the number is negative"
# • თუ ნულია, დაბეჭდოს: "the number is zero"
# num = int(input("Enter your number: "))

# if num >0:
#     print("the number is positive")
# elif num <0:
#     print("the number is negative")
# elif num == 0:
#     print("the number is zero")
# 2) ცვლადში შეინახეთ პაროლი. შემდეგ მომხმარებელს შემოატანინეთ პაროლი. იქამდე გამოუტანეთ
# "incorrect password" სანამ მომხმარებელი სწორად არ შემოიტანს პაროლს. სწორად შემოტანის შემთხვევაში გამოიტანეთ "correct password" (გამოიყენეთ while loop)

password = "1234"
password1 = (input("Enter your password: "))
while password != password1:
    print("incorrect password")
    password2 = input("Enter your password: ")
print("correct password")