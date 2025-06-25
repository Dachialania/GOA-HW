# 2) კომენტარის სახით ახსენით რატომ ვიყენებთ Slicing-ს Python-ში.
# slicing-ს ვიყენებთ python ში რომ ლისტიდან ან სტრინგიდან ამოვჭრათ გარკვეული ნაწილი ლისტის დროს გვიბრუნებს ისევ ლისტის სახით და სტრინგის დროს ჩვეულებრივად

# 3) შექმენით რიცხვების სია, სადაც შენახული გექნებათ 10 რიცხვი. Slicing-ის მეშვეობით გამოიტანეთ ამ სიის პირველი ხუთი რიცხვი და გამოიტანეთ ტერმინალში.
# numbers = [1,2,3,4,5,6,7,8,9,10]
# print(numbers[:5])

# 4) ცვლადში შეინახეთ სიტყვა "Goal-Oriented Academy".
# გამოიყენეთ Slicing რათა აქედან დაბეჭდოთ მხოლოდ სიტყვა "Academy".
# academy = "Goal-Oriented Academy"
# print(academy[14:])

# 5) ცვლადში შეინახეთ სიტყვა "Goal-Oriented Academy".
# გამოიყენეთ Slicing რათა აქედან დაბეჭდოთ მხოლოდ სიტყვა "Oriented".
# academy1 = "Goal-Oriented Academy"
# print(academy1[5:13])

# 6) ცვლადში შეინახეთ თქვენი გვარი. ინდექსინგის საშუალებით გამოიტანეთ თქვენი გვარის პირველი, ბოლო და შუა ასოები.
# last_name = "Alania"
# l1 = last_name[:1]
# l2 = last_name[3:4]
# l3 = last_name[5:6]
# print(l1,l2,l3)
# 7) შექმენით სია colors = ["Black", "Yellow", "Blue", "Purple", "Orange"]

# სიიდან გამოიტანეთ მხოლოდ Yellow და Black.
# colors = ["Black", "Yellow", "Blue", "Purple", "Orange"]
# print(colors[:2])

# 8) შეინახეთ ცვლადში "Hello, World!". Slicing-ის საშუალებით ამ სტრინგიდან  ამოიღეთ ცალკე სიტყვა "Hello" და ცალკე სიტყვა "World!". 
# შეინახეთ ისინი ცვლადებში და გამოიტანეთ ეკრანზე.
word = "Hello, World!"
W1 = word[:6]
w2 = word[6:]
print(W1,w2)