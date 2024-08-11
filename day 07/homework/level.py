
# მომხმარებლისგან 5 რიცხვის მიღება
numbers = []
for i in range(5):
    num = float(input(f"შეიყვანეთ რიცხვი {i + 1}: "))
    numbers.append(num)

# არითმეტიკული ოპერაციების გაკეთება
sum_result = sum(numbers)
difference_result = numbers[0]
for num in numbers[1:]:
    difference_result -= num

product_result = 1
for num in numbers:
    product_result *= num

quotient_result = numbers[0]
for num in numbers[1:]:
    if num != 0:
        quotient_result /= num
    else:
        quotient_result = "გარკვევადი - არ შეიძლება გაყოფა ნულზე"
        break

floor_div_result = numbers[0]
for num in numbers[1:]:
    if num != 0:
        floor_div_result //= num
    else:
        floor_div_result = "გარკვევადი - არ შეიძლება გაყოფა ნულზე"
        break

modulus_result = numbers[0]
for num in numbers[1:]:
    if num != 0:
        modulus_result %= num
    else:
        modulus_result = "გარკვევადი - არ შეიძლება გაყოფა ნულზე"
        break

# შედეგების გამოქვეყნება
print(f"ჯამი: {sum_result}")
print(f"სხვაობა: {difference_result}")
print(f"ნამრავლი: {product_result}")
print(f"განაყოფი: {quotient_result}")
print(f"დახლებულობა: {floor_div_result}")
print(f"ნარჩენი: {modulus_result}")





