def find_short(s):
    list1 = s.split(" ")
    # `split(" ")` მეთოდი ხსნის სტრინგს სიტყვებად, სუფთა პუნქტუაციისგან განსაზღვრული ცარიელი სივრცით.

    word_len = len(list1[0])
    # აქ `word_len` გაწვდილი არის პირველი სიტყვის სიგრძე, რაც ნიშნავს რომ მეთოდი იწყებს შედარებას პირველი სიტყვით.

    for i in list1:
        if len(i) < word_len:
            word_len = len(i)
    # `for` ციკლი გადის თითოეულ სიტყვაზე `list1` სიაში. თუ რომელიმე სიტყვა მოკლედ არის ვიდრე მიმდინარე მინიმალური სიგრძე, მაშინ `word_len` განახლდება.

    return word_len
    # საბოლოოდ, ფუნქცია აბრუნებს მოკლე სიტყვას სიგრძეს.

print(find_short("bitcoin take over the world maybe who knows perhaps"))
# ფუნქცია გამოუწვდოს მოკლე სიტყვის სიგრძეს დანაწყვეტილი ტექსტიდან.

# 1. გამოგყავით სტრინგი დანაწყვეტილი ღირებულებით
s1 = "apple,banana,orange"
result1 = s1.split(",")
print(result1)  # ['apple', 'banana', 'orange']

# 2. გამოგყავით სტრინგი წერტილით
s2 = "www.example.com"
result2 = s2.split(".")
print(result2)  # ['www', 'example', 'com']

# 3. გამოგყავით სტრინგი ცარიელი სივრცით
s3 = "Hello World How Are You"
result3 = s3.split()
print(result3)  # ['Hello', 'World', 'How', 'Are', 'You']

# 4. გამოგყავით სტრინგი ორი ცარიელი სივრცით
s4 = "Hello  World  How"
result4 = s4.split("  ")
print(result4)  # ['Hello', 'World', 'How']

# 5. გამოგყავით სტრინგი სლეშით
s5 = "folder1/folder2/folder3"
result5 = s5.split("/")
print(result5)  # ['folder1', 'folder2', 'folder3']

# 6. გამოგყავით სტრინგი ახალ ხაზზე
s6 = "line1\nline2\nline3"
result6 = s6.split("\n")
print(result6)  # ['line1', 'line2', 'line3']

# 7. გამოგყავით სტრინგი ტაბულატორით
s7 = "name\tage\tcity"
result7 = s7.split("\t")
print(result7)  # ['name', 'age', 'city']

# 8. გამოგყავით სტრინგი გამოტანილი სიმბოლოთი
s8 = "key:value"
result8 = s8.split(":")
print(result8)  # ['key', 'value']

# 9. გამოგყავით სტრინგი მარყუჟით
s9 = "one-two-three"
result9 = s9.split("-")
print(result9)  # ['one', 'two', 'three']

# 10. გამოგყავით სტრინგი ზემოთნაწყვეტილი სივრცით
s10 = "split-this-string"
result10 = s10.split("-")
print(result10)  # ['split', 'this', 'string']
