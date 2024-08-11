
#1. მომხმარებლისგან მონაცემების მიღება
first_name = input("შეიყვანეთ სახელი: ")
last_name = input("შეიყვანეთ გვარი: ")

# ერთიანი წინადადების გამოქვეყნება
print(f"გამარჯობა, {first_name} {last_name}!")


#2. საკუთარი რიცხვის შექმნა
my_number = 10  # თქვენთვის სასურველი რიცხვი

# მომხმარებლისგან რიცხვის მიღება
user_number = float(input("შეიყვანეთ რიცხვი: "))

# რიცხვების ჯამის გამოთვლა და გამოქვეყნება
sum_of_numbers = my_number + user_number
print(f"რიცხვების ჯამი: {sum_of_numbers}")



#3. სამი რიცხვის შემუშავება
num1 = 5
num2 = 15
num3 = 25

# რიცხვების ჯამის გამოთვლა და მათი რაოდენობით გაყოფა
average = (num1 + num2 + num3) / 3
print(f"რიცხვების საშუალო: {average}")

#4. სტრინგის მიღება და გამრავლება ხუთზე
string_input = input("შეიყვანეთ სტრინგი: ")
string_result = string_input * 5
print(f"სტრინგის გამრავლებული შედეგი: {string_result}")  # სტრინგის ხუთჯერ გამრავლებული შედეგი

# რიცხვის მიღება და გამრავლება ხუთზე
number_input = float(input("შეიყვანეთ რიცხვი: "))
number_result = number_input * 5
print(f"რიცხვის გამრავლებული შედეგი: {number_result}")  # რიცხვის ხუთჯერ გამრავლებული შედეგი


#5. ორი რიცხვის მიღება
num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))

# კალკულაციის შედეგების გამოთვლა
sum_result = num1 + num2
difference_result = num1 - num2
product_result = num1 * num2
quotient_result = num1 / num2 if num2 != 0 else "გარკვევადი - არ შეიძლება გაყოფა ნულზე"

# შედეგების გამოქვეყნება
print(f"ჯამი: {sum_result}")
print(f"სხვაობა: {difference_result}")
print(f"ნამრავლი: {product_result}")
print(f"განაყოფი: {quotient_result}")

