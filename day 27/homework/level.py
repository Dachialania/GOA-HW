# 2) მოიყვანეთ მაგალითები და ახსენით თუ რატომ არის სტრინგი - Immutable და სია - Mutable.
# ამასთანავე ახსენით თუ რას ეწოდება Mutable და Immutable.
# month = "august" 
# month[0] = "A"
# print(month)
# ჩვენ ეს რომ დავპრინტოთ გამოოგვიტანს error - ს რადგან სტრინგს ვერ შევუცვლით ინდექს იმიტომ რომ ეს არის imutable რომელიც ნიშნავს შეუცვლელი
# fruits = ["cherry", "banana", "apple"]
# fruits[2] = "orange"
# print(fruits)
# ლისტებში ჩვენ გვაქვს მოცემული ელემენტები და ჩვენ შეგვიძლია რომ შევცვალოთ ლისტში მოცემული ელემენტები სხვა ელემენტით ინდექსების მიხედვით ამიტომ ეს ნიშნავს mutable შეცვლადი

# 3) მომხმარებელს შემოატანინეთ თავისი სახელი, გვარი, ID ნომერი და ეროვნება. ეს ყოველივე შეინახეთ User_info ცვლადში. ჯერ მთლიანი სია დაბეჭდეთ, 
# შემდეგ კი ინდექსინგის საშუალებით გამოიტანეთ სიის თითოეული ელემენტი ტერმინალში.
# name = input("ჩაწერეთ თქვენი სახელი: ")
# last_name = input("ჩაწერეთ თქვენი გვარი: ")
# id_number = int(input("ჩაწერეთ თქვენი id ნომერი: "))
# Nationality = input("ჩაწერეთ თქვენი ეროვნება: ")
# user_info = [name, last_name, id_number, Nationality]
# print(user_info)
# print(user_info[0])
# print(user_info[1])
# print(user_info[2])
# print(user_info[3])

# 4) შექმენით Vending Machine პროგრამა.

# შექმენით Vending Machine სია სადაც მინიმუმ 10 ცალ პროდუქტს დაამატებთ. მომხმარებელი უნდა ირჩევდეს პროდუქტის ინდექსს და 
# შემდეგ თქვენ პროდუქტის დასახელება უნდა გამოუტანოთ ტერმინალში. (პირობაში დეტალები არ მიწერია, ასერომ ეცადეთ რაც შეიძლება დახვეწილი და მომხმარებლისთვის
# მოსახერხებელი პროგრამა შექმნათ)
# Vending_machine = ["phone","TV","mouse","keyboard","chair","desk","glasses","umbrella","coca-cola","treasure"]
# print(Vending_machine)
# number = int(input("ჩაწერეთ ამოსარჩევი ციფრი: "))
# for i in range(10):
#     if i == number:
#         print(Vending_machine[i])
  
# 5) შექმენით Fruits სია: 
# Fruits = ["Strawberry", "Mango", "Melon", "Cherry"]
# სიის მეოთხე ელემეტი ჩაანაცვლეთ "Watermelon"-ით, მეორე ელემენტი კი "Pear"-ით. ტერმინალში დაბეჭდეთ სიის თავდაპირველი და საბოლოო სახე.
# Fruits = ["Strawberry", "Mango", "Melon", "Cherry"]
# print(Fruits)
# Fruits[2] = "pear"
# Fruits[3] = "watermelon"
# print(Fruits)


# 6) რამდენიმე ცვლადში შინახეთ სხვადასხვა სიტყვა. ამ სიტყვების გამოყენებით ააწყვეთ ერთი მთლიანი სიტყვა. მაგ.
# ("Moon", "light"  "Moonlight")
# sentence = ["დაჩი", "16", "სენაკში", "ალანია"]
# print(f"ჩემი სახელია {sentence[0]} და ჩემი გვარი არის {sentence[3]}, მე ვარ {sentence[1]} წლის და ვცხოვრობ ქალაქ {sentence[2]} ")

