# 1) სიტყვა "Motorcycle"-იდან Slicing-ის მეშვეობით გამოიტანეთ ცალკე "Motor" და ცალკე "cycle"
bike = "motorcycle"
print(bike[:5])
print(bike[5:])

# 2) fruits = ["Mango", "Melon", "Cherry", "Pear", "Watermelon"]

# მოცემული სიიდან გამოიტანეთ ელემენტები - Cherry, Pear, Watermelon.

fruits = ["Mango", "Melon", "Cherry", "Pear", "Watermelon"]
print(fruits[2:])

# 3) colors = ["red", "green", "blue", "black", "White", "Brown"]

# მოცემული სიიდან გამოიტანეთ მხოლოდ red, green, blue
colors = ["red", "green", "blue", "black", "White", "Brown"]
print(colors[:3])

# 4) ახსენით თუ რატომ გამოდის პასუხი სიის სახით, მას შემდეგ რაც სიაზე ვიყენებთ Slicing-ს.]
# slicing სიიდან გარკვეულ  ნაწილს ამოჭრის, ჩვენ სიას როდესაც ვუკეთებთ slicing თვითონ სია აბრუნებს სიის სახეს ისევ 