# #1 გაქვთ ონლაინ მაღაზია, როდესაც მომხმარებელი შემოდის პროგრამის გაშვებისას უნდა
# გამოუჩნდეს მენიუ მაგალითად: “გამარჯობა” თქვენ იმყოფებით მაღაზია SpaceX-ში, პროდუქტები:
# რაკეტა - 15000$, ხომალდი - 25000$, ჩაფხუტი - 5000$ და ა.შ. მომხმარებელს უნდა ჰკითხოთ
# რომელი ნივთები უნდა და დაუთვალოთ რა დაუჯდება ჯამურად, თუ დაგეთანხმებათ უნდა მიჰყიდოთ
# ნივთები თუ უარს იტყვის შეთავაზებაზე უნდა დაასრულოთ მუშაობა.



# print("გამარჯობა, თქვენ იმყოფებით მაღაზია SpaceX-ში")

# produktebi= {
#     "raketa": 15000, 
#     "xomaldi": 25000, 
#     "chafxuti" : 5000 }
# print(f" ჩვენი პროდუქტებია: {produktebi}")

# sasurveli_nivtebi=[]
# nivti=input("შემოიყვანეთ სასურველი ნივთის დასახელება, თუ აღარ გსურთ მეტი ნივთი დაწერეთ დასრულება")
# while nivti != "დასრულება":
#     sasurveli_nivtebi.append(nivti)
#     nivti=input("შემოიყვანეთ სასურველი ნივთის დასახელება, თუ აღარ გსურთ მეტი ნივთი დაწერეთ დასრულება")


# total=0
# for nivti in sasurveli_nivtebi:
#     if nivti == "raketa":
#         total += 15000
#     elif nivti == "xomaldi":
#         total += 25000
#     elif nivti == "chafxuti":
#         total += 5000

# print(f" ჯამში თქვენი ნივთების ფასია: {total}, გნებავთ?")
# answer=input("კი ან არა")
# if answer == "კი":
#     print("თქვენ შეიძინეთ ნივთები")
# else:
#     print("მუშაობა დასრულებულია")





# #2 While loop და FOR LOOP-ის გამოყენებით დაწერეთ ციკლი, რომელიც დაბეჭდავისას, გვერდით
# დაუწერს რიცხვს ლუწია თუ კენტი 20-მდე. (დაწერეთ ორივე ვარიანტი)

for i in range(20):
    if i==0:
        print(str(i) + " ნული")     #  print(f" {i}  + ნულია")
    elif i%2==0:
        print(str(i) + " ლუწია")
    else:
        print(str(i) + " კენტია")


i=0
while i<20:
    if i==0: 
        print(str(i) + " ნული")
    elif i%2==0:
        print(str(i) + " ლუწია")
    else:
        print(str(i) + " კენტია")
    i+=1


print(f" {i}  + ნულია")

# #3 გამოითვალეთ თითოეული სტუდენტის საშუალო არითმეტიკული ქულა და დააბრუნეთ მისთვის
# შესაფერისი ნიშანი:
Students = {
"Ana": [89,66,12,75,11],
"Giorgi": [67,72,90,91,55],
"Levant": [49,36,88,98,34],
"Veronika": [99,88,32,65,99],
"Nika": [77,81,41,73,99] }

saxelebi = list(Students.keys())
qulebi = list(Students.values())

for i in range(len(saxelebi)):
    saxeli = saxelebi[i]
    studentis_qulebi  = qulebi[i]
    jami=0
    for i in studentis_qulebi:
        jami+=i
    
    sashualo=jami/len(studentis_qulebi)
    print(f"saxeli - {sashualo}")




# #4 დაწერეთ ციკლი, რომელიც მოითხოვს მომხმარებლისგან ასაკის შეყვანას, თუ შეყვანილი
# მონაცემი არ იქნება რიცხვური ტიპის, მაშინ ციკლი დატრიალდეს და თავიდან კითხოს, სხვაგვარად
# დაუანგარიშოს დაბადების თარიღი.

# from datetime import date

# while True:
#     asaki = input("შემოიყვანეთ ასაკი")
#     if asaki.isdigit():
#         current_year = date.today().year
#         birth_date = current_year-int(asaki)
#         print(f"თქვენი დაბადების თარიღია {birth_date}")
#         break



# #5 While ციკლის მეშვეობით დაითვალეთ მოცემული მასივის:
mylist = range(100)
# *მეორე ხარისხი
# *მესამე ხარისხი

my_new_list = []
mylist = list(range(100))
for i in range(100):
    kvadrati=i**2
    my_new_list.append(kvadrati)


my_second_list = []
for i in range(100):
    kubi=i**3
    my_second_list.append(kubi)


# #6 FOR ციკლის/ციკლების გამოყენებით შექმენი გამრავლების ტაბულა და ტერმინალში გამოიტანე
# მსგავსი ფორმატით:
# 1 2 3 4 5 6 7 8 9 10
# 2 4 6 8 10 12 14 16 18 20
# 3 6 9 12 15 18 21 24 27 30
# 4 8 12 16 20 24 28 32 36 40
# 5 10 15 20 25 30 35 40 45 50
# 6 12 18 24 30 36 42 48 54 60
# 7 14 21 28 35 42 49 56 63 70
# 8 16 24 32 40 48 56 64 72 80
# 9 18 27 36 45 54 63 72 81 90
# 10 20 30 40 50 60 70 80 90 100

ricxvebi=[]
for i in range(1,11):
    for k in range(1,11):
        ricxvebi.append(i*k)
        
        
for i in range(len(ricxvebi)):
    print(ricxvebi[i], end="\t")
    if (i+1) % 10 == 0:
        print()

# #7 გააანალიზე კოდის ფრაგმენტი და შემდეგ გაასწორე შეცდომები, ასევე დაწერე ახსნა:
# numbers = ["1", "2", "3", "4"]
# total = 0
# for n in numbers:
#     total += n
# print("Total:", total)

# რადგან numbers სიაში რიცხვები string ტიპისაა, მათ მიმატებას პირდაპირ ვერ შევძლებთ. ჯერ უნდა ვაქციოთ int-ad. 

numbers = ["1", "2", "3", "4"]
total = 0
for n in numbers:
    total += int(n)
print("Total:", total)


# #8 გამოიყენე FOR ციკლი რომელიც მიწვდება data ყველა ელემენტს და დაწერე შემდეგი ლოგიკა, თუ
# ელემენტი არის სტრინგი და შეიცავს მხოლოდ რიცხვს გადააქციე რიცხვად და შეინახე total-ში, თუ
# რიცხვია პირდაპირ შეინახე total-ში, თუ სხვა ტიპის მონაცემთა ტიპია გამოტოვე. ბოლოს დაბეჭდე
# სრული ჯამი.

data = ["5", 0, "3", True, "", 2, "x", False]
total = 0

for i in data:
    if type(i) == str and i.isdigit():
        total += int(i)
    elif type(i) == int:
        total += i
    else:
        continue

print(total)


# #9 დაწერეთ FOR LOOP სადაც მიწვდებით მონაცემებს, თუ მნიშვნელობა არის სტრინგი და შეიცავს
# მხოლოდ რიცხვს გამოიყენე კასტინგი და შეინახე, თუ ინთეჯერია შეინახე პირდაპირ, თუ ბულიენია
# გადააქციე და შეინახე (მხოლოდ True) სხვა ყველა ტიპის მონაცემი გამოტოვე.

transactions = {
"გიო": "100",
"ნიკა": 50,
"აკაკი": "30a",
"ლევანი": 0,
"ანა": "70",
"მარი": True
}
total = 0


for i in list(transactions.values()):
    if type(i) == str  and i.isdigit():
        total += int(i)
    elif type(i) == int:
        total += i
    elif type(i) == bool:
        total += int(i)
    else:
        continue

print(total)






# #10 შექმენი პროგრამა (თამაში) სადაც მომხმარებელი შეძლებს გამოიცნოს შენი ჩაწერილი რიცხვი,
# მომხმარებელი წერს ციფრებს და ცდილობს გამოიცნოს შენი რიცხვი, დიაპაზონი 0-დან 51-მდე, თუ
# მომხმარებელმა ჩაწერა ამ დიაპაზონს გარეთ უნდა გამოუტანო შეტყობინება რომ “რიცხვი სცდება
# არეალს”, თუ ჩაწერა “exit” გამორთე თამაში, უნდა დაუთვალო მცდელობების რაოდენობა და
# გამოიტანო შეტყობინება: "გილოცავ გამოიცანი XX რიცხვი, მცდელობა:XX"

counter=1
chemi_ricxvi = 5
while True:

    ricxvi=input("შემოიყვანე რიცხვი 0-დან 51-მდე")
    if ricxvi =="exit":
        break
    elif int(ricxvi) < 0  or int(ricxvi) > 50:
        print("შემოყვანილი რიცხვი სცდება არეალს")
    elif int(ricxvi) == chemi_ricxvi:
        print(f"გილოცავ, გამოიცანი {counter} ცდაზე")
        break
    counter+=1


    