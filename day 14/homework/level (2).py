#1
list = ["support","trundle","dasanerfia"]
print(list)

list0 = [1,5,2,3,5,23,52]
print(len(list0))

list1 = ["abc", 34, True, 40, "male"]
print(list1)


list2 = [1,2,3,24,]
print(type(list2))


list3 = list(("apple", "grass", "ice cream"))
print(list3)
#2
list = [1,23,3,2]
print(list[1])


list0 = ["grass","touch"]
print(list0[-1])

list1  = [1,3,2,5,4,2,3,5,7,4,2]
print(list1[2:6])

list2 = [1,3,2,4,5,23,5,23,52,32,5,2]
print(list2[2:])

list3 = ["touch","grass"]
if "touch" in list3:
    print("grass has been touched")



list = [1,3,5,7,9]
list[1] = 11
print(list)

list0 = [1,3,5,6,7,8,2]
list0[2:4] = 2,4
print(list0)

list1 = [2,3,24,4,2,3]
list1[1:2] =  4,5
print(list1)

list2 = [2,3,4,5,6]
list2[1:3] = [1]
print(list2)


list3 = [2,3,4,2,5]
list3.insert(2,5)
print(list3)



2
1
names = ["dachi, luka, dito, nino, archili"]

print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])

numbers = [1,2,3,4,5,6,7,8,9,10]

print(numbers[0])
print(numbers[9])


3
numbers = []
for i in range(10,21):
    numbers.append(i)
newnumber = []
for x in numbers:
   if x % 2 == 0:
        newnumber.append(1)
   else:
       newnumber.append(i)
print(newnumber)

4
name = input("please enter your name: ")
lastname = input("please enter your lastname: ")
age = input("please your age: ")
adress =  input("please enter your adress: ")

newlist = []
newlist.insert(1,name)
newlist.insert(2,surname)
newlist.insert(3,age)
newlist.insert(4,adress)
print(newlist)

#5
surname = "alania"
for i in surname:
    print(i)