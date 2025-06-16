# 2) კომენტარის სახით დაწერეთ თუ რა დანიშნულება აქვს type() ფუნქციას და რატომაა მისი გამოყენება მოხერხებული.
# type() ფუნქცია გვეხმარება დავადგინოთ თუ რა კლასისაა მონაცემი.

# 3) ჩამოწერეთ ყველა ის ფუნქცია რომელიც “Data Conversion”-ს მოიცავს. გატესტეთ თითოეული ყველა ნასწავლ მონაცემთა ტიპზე.
# ჩვენ ჯერ ჯერობით ნასწავლი გვაქვს 1)string 2) integer 3) float 4) boolean
# 1)string
# full_name = " dachi alania"
# age = " 16"
# city = " senaki"
# print(f"my name is {full_name}, i am {age} years old and i live in {city}.")


# 2)integer
# num1 = 16
# num2 = 5
# result = num1 * num2
# print(result)


# 3)float
# num1 = 2.5
# num2 = 8.5
# result = num1 * num2
# print(result)

# 4)bolean
# bolean = True and False or True or False and True and True
# print(bolean)

# 4) ცვლადებში შეინახეთ თქვენი სახელი,  გვარი და ასაკი (Integer) . ტერმინალში გამოიტანეთ წინადადება - რომელსაც კონკატინაციის შედეგად მიიღებთ. ვიცით რომ String-სა და Integer-ს შორის მათემატიკურ ოპერაციას ვერ შევასრულებთ, შესაბამისად დაწერეთ ისეთი კოდი, რომ Error-ების გარეშე გაეშვას ტერმინალში.

# name = "dachi"
# last_name = "alania"
# age = 16
# print("i am " + name + " "  + last_name + " and i am " + str(age) + " years old" )

# 5) მომხმარებელს შემოატანინეთ 5 რიცხვი. დაწერეთ პროგრამა, რომელიც გამოთვლის და დაბეჭდავს ამ რიცხვების საშუალო არითმეტიკულს. 
# num1 = 10
# num2 = 20
# num3 = 15
# num4 = 25
# num5 = 45
# result = num1 + num2 + num3 + num4 + num5
# result1 = result / 3
# print(result1)

#  (საშუალო არითმეტიკული - რიცხვთა ჯამის განაყოფი რიცხვების რაოდენობაზე)

# 6) მომხმარებელს შემოატანინეთ ტემპერატურა ცელსიუსში. დაწერეთ პროგრამა, რომელიც მომხმარებლის მიერ შემოტანილ ტემპერატურას გადაიყვანს ფარენგეიტში და დაბეჭდეთ საბოლოო შედეგი. (მოიძიეთ ფორმულა ინტერნეტში)


# celsius = float(input("enter your temperature in celsius: "))
# F =  celsius * 9/5 + 32 
# print(F)


# 7) მეხუთე დავალების მსგავსად, შემოატანინეთ მომხმარებელს ტემპერატურა, თუმცა ამჯერად - ფარენგეიტში. 
# შემდეგ კი დაწერეთ პროგრამა, რომელიც შემოტანილ ტემპერატურას ცელსიუსში გადაიყვანს და საბოლოოდ დაბეჭდეთ შედეგი.

# farengeith = float(input("enter your temperature in celsius: "))
# C = farengeith - 32 
# C1 = farengeith / 0.5
# print(C1)
# print(type(3.0))