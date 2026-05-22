# 1. შეინახეთ ცვლადებში ცვლადების ტიპები მათი მნიშვნელობების ნაცვლად
var1 = 1
var2 = -1
var3 = True

var1=type(var1)
var2=type(var2)
var3=type(var3)

print(var1,var2,var3)

# 2. შეცვალეთ ცვლადების ტიპები (type casting-ის მეშვეობით)
var4 =False # გადაიყვანეთ Float -ში
var5 =3 # გადაიყვანეთ Float -ში
var6 = {"key":"value", "key1":"value", "key3":"value"} # გადაიყვანეთ list -ში

var4= float(var4)
var5= float(var5)
var6= list(var6)

print(var4, var5, var6)

# 3. შექმენით შესაფერისი ტიპის ცვლადები მონაცემებისთვის.
group = 2
name = "Python2023"
count= 35
male= 22
female= 13
students=( "Student1", "Student2", "Student3", "Student4", "Student5")
ages = (24,33,15,45,42)


# 4. დააფორმატეთ სტრიქონი და გამოითვალეთ თქვენი ასაკი
birth_year = 2006 # ჩაწერეთ წელი
name = "ინგა" # ჩაწერეთ სახელი
surname = "ბაღდუაშვილი" # ჩაწერე გვარი
current_year = 2026
# # უნდა მიიღოთ შემდეგი წინადადება - მე ‘სახელი’ ‘გვარი’ დავიბადე ‘ამ წელს’ შესაბამისად ვარ
# ‘ამდენი წლის’
print("მე " + name + " " + surname + " დავიბადე " + str(birth_year) + " წელს, შესაბამისად ვარ " + str(current_year-birth_year) +" წლის.")

# 5. გამოითვალეთ მომხრეთა და მოწინააღმდეგეთა პროცენტი და აჩვენეთ ორივე.
# (შეეცადეთ დაამრგვალოთ პროცენტები მეასედებამდე)
# მაგალითი:
# YES: 1234 = 34.80%
# NO: 2312 = 65.20%
Yes = 119
No = 82

Yes_p=(Yes*100)/(Yes+No)
Yes_p=round(Yes_p,2)
No_p=((No*100)/(Yes+No))
No_p=round(No_p,2)
print(Yes_p, No_p)

# 6. გადაიყვანეთ 3670 წამი საათებად და წუთებად
seconds = 3670
# დაბეჭდეთ: "X საათი Y წუთი Z წამი"

print(str(seconds//3600)+ " საათი " + str((seconds%3600)//60) +" წუთი " + str((seconds%3600)%60) +" წამი")
 


# 7. გამოიტანეთ სტრიქონის პირველი და ბოლო ასო
text = "Python"
text=list(text)
print(text[0], text[-1])

# 8. გამოითვალეთ სასწავლო საგნის შეფასების პროცენტული წილი
math = 45
total = 60
# დაბეჭდეთ: "პროცენტი: XX%"
print("პროცენტი: " + str(math/total*100)+ "%")

# 9. გამოითვალეთ ასაკი მომავალ წელს
birth_year = 2000
current_year = 2025
# დაბეჭდეთ ფორმატში:
# “მომავალ წელს შენ იქნები XX წლის”
print("მომავალ წელს შენ იქნები "+ str(current_year-birth_year+1) + " წლის.")

# 10. 350 წუთი რამდენი საათია და რამდენი წუთი დარჩება გამოიტანეთ
minutes = 350
# მაგალითი: “X საათი და XX წუთი”

print(str(minutes//60) + " საათი და " + str(minutes%60) + " წუთი.")