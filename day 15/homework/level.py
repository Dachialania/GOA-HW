# 2) გახსენეთ და დაწერეთ თუ რა შედეგს ვიღებს შედარების და ლოგიკური ოპერაციების გამოყენებისას.
# a = 10
# b = 5

# print(a > b)              # True
# print(a < b)              # False
# print(a > b and b < 2)    # False
# print(a > b or b < 2)     # True


# 3) ჩამოწერეთ ყველა შესაძლო ლოგიკური გამოსახულება (and და or ოპერატორების გამოყენებით)
# print(True and False or True and True and False or False and False )
# print(True)
# print(False)
# 4)  რას გამოიტანს მოცემული კოდები?

# print(False or True and True and False)  False

# print(True and False or False or True) True

# print(True or True and False or True or False and True or False) True

# 5) დაწერეთ სახლის გაგრილების სისტემის პროგრამა.
# ვთქვათ, როდესაც სახლში ტემპერატურა 30 გრადუსს ასცდება - ავტომატურად უნდა ჩაირთოს გაგრილების სისტემა. იმის გასაგებად თუ რა ტემპერატურაა სახლში,
#  მომხმარებელს იგი შემოატანინეთ input() ფუნქციის მეშვეობით. (გამოიყენეთ მხოლოდ ლოგიკური ოპერატორები)

# temperature1 = float(input("enter your temperature: "))
# temperature = 30.0

# if temperature1 >= temperature:
#     print(True)
# else:
#     print(False)

# HARD LVL:
# 6) დაწერეთ ოთახის გაგრილების სისტემის პროგრამა, but there’s a twist:

# ჩათვალეთ, რომ პროგრამა მხოლოდ იმ შემთხვევაში აღიქვამს ოთახის ტემპერატურას, თუ იგი ფარენგეიტშია გადმოცემული. (სისტემა ჩაირთვება მაშინ, როდესაც ტემპერატურა 89.6 ფარენგეიტს ასცდება). 
# ერთადერთი გასათვალისწინებელი ფაქტი ის არის, რომ მომხმარებელს ოთახის ტემპერატურა გრადუსებში შემოაქვს. 

# ეცადეთ დაწეროთ პირობის მიხედვით ისეთი ოთახის გაგრილების სისტემის პროგრამა, რომელიც სწორად იმუშავებს 


# temperature = float(input("enter your temperrature: "))
# farengeith = 89.5 -32
# result = farengeith * 5
# result1 = farengeith / 9
# result2 = 32.0

# if temperature == result2:
#     print("it's normal temperature")
# elif temperature > result2:
#     print("it's very hot")
# else:
#     print("A little chilly.")