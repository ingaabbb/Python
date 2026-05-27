#1 დაწერეთ პირობა, რომელიც გაარკვევს შემოტანილი ასო არის თანხმოვანი თუ ხმოვანი
# მაგალითი:
# შემოიტანე სიმბოლო: ბ "ბ" თანხმოვანია
# =====================
# შემოიტანე სიმბოლო: ი "ი" ხმოვანია
# =====================

# xmovnebi = "aeiou"
# qartuli_xmovnebi = "აეიოუ"

# while True:
#     simbolo = input("შემოიტანე სიმბოლო")
#     if len(simbolo) == 1 and simbolo.isalpha():
#         if simbolo in xmovnebi or simbolo in qartuli_xmovnebi:
#                 print(f"{simbolo} ხმოვანია")
#         else:
#             print(f"{simbolo} თანხმოვანია")
#         break
#     else:
#         print("შემოიტანეთ მხოლოდ სიმბოლო")







#2 დაწერე პირობა რომელიც for ციკლის გამოყენებით გამოიტანს რიცხვებს 10-დან 0-მდე

# for i in range(10,0,-1):
#      print(i)

#3 დაწერეთ ციკლი რომელიც დაბეჭდავს ლისტში მყოფ უდიდეს 3 რიცხვს და მათ ინდექსებს
# import random
# lst = [random.randint(1,20) for _ in range(10)] # ქმნის და ინახავს random მონაცემებს [1,4,2,3,6,5]
# print(lst)
# მაგალითი:
List = [3, 14, 4, 1, 2, 11, 12, 18, 7, 18]
# მონაცემი 1: 18
# მონაცემი 2: 18
# მონაცემი 3: 14
count=1
Max_index = []
while count < 4:
    Max = List[0]
    for i in range(len(List)):
        if List[i] > Max and i not in Max_index :
            Max = List[i]
            Max_indx = i
            
    print(f"მონაცემი {count}: {Max}")
    count += 1
    Max_index.append(Max_indx)
    



# #4 დაწერეთ ციკლი რომელიც დაბეჭდავს ოთხუთხედს “#” (ასეთს) მოცემული სიმაღლისა და სიგანის
# მიხედვით
# მაგალითი:
# width=5
# height=2

width=2
height=5
for i in range(height):
    for k in range(width):
        print('#', end="")
    print()



#5 მომხმარებელს შემოყავს ორი რიცხვი x & y შექმენით ფუნქცია, რომელიც მიიღებს ამ ორ
# პარამეტრს და დაბეჭდავს ყველა არითმეტიკულ ოპერაციას
# მაგალითი:
# 5 + 2 = 7
# 5 - 2 = 3
# 5 * 2 = 10
# 5 / 2 = 2.5
# 5 // 2 = 2
# 5 % 2 = 1

def function(a,b):
    jami = a + b
    sxvaoba = a - b
    namravli = a * b
    gayofa = a / b
    mtelisPovna = 5 // 2
    nashti = a % b
    return jami, sxvaoba, namravli, gayofa, mtelisPovna, nashti

print(function(5,2))


#6 გადააქციეთ დავალება #4 ფუნქციად,
# რომელსაც ექნება 2 პარამეტრი სიმაღლე, სიგანე

def otxkutxedi(width, height):
    for i in range(height):
        for k in range(width):
            print('#', end="")
        print()



#7 დაწერეთ ფუნქცია, რომელიც მიიღებს 2 პარამეტრს:
# სტრიქონს და სიმბოლოს ფუნქციამ უნდა დაითვალოს თუ რამდენჯერ გვხვდება სიმბოლო სტიქონში.
# მაგალითი:
# in_str("John and Jane Doe", "J")
# >>> Character "J" in given string: 2 times

def simbolos_raodenoba(a,b):
    counter = 0
    for i in a:
          if i == b:
            counter += 1
    return f" Character {b} in given string: {counter} times"    
    
print(simbolos_raodenoba("John and Jane Doe", "J"))



#8 დაწერეთ ფუნქცია რომელიც დაითვლის სიტყვების რაოდენობას წინადადებაში.
# მაგალითი:
# wc("რამდენიმე სიტყვა რომლის დათვლასაც ვაპირებთ")
# >>> სიტყვების რაოდენობა წინადადებაში შეადგენს 5-ს.

def sityvata_raodenoba(winadadeba):
    winadadeba_list = list(winadadeba.split())
    raodenoba = len(winadadeba_list)
    return(raodenoba)
print(sityvata_raodenoba("gamarjoba me var"))



#9 შექმენი თამაში hangman სიტყვის გამოცნობა...
# კომპიუტერი ირჩევს “შემთხვევით” სიტყვას და მომხმარებელს აქვს 10 ცდა სიტყვის გამოსაცნობად,
# მომხმარებელს აქვს ასოების ჩაწერის უფლება და ასევე სიტყვის ჩაწერის უფლება სრულად, თუ
# სიტყვას 10 ცდაში გამოიცნობს გამოიტანოს “გილოცავ” თუ ვერ გამოიტანოს “თქვენ დამარცხდით”
# თამაშის გამორთვა “exit”

#10 შექმენი პატარა თამაში სადაც მომხმარებელს აქვს ორი არჩევანი “მარჯვენა” ან “მარცხენა”
# პროგრამამ შემთხვევითობის პრინციპით უნდა გაანაწილოს რომელია სწორი “მარჯვენა” თუ
# “მარცხენა”, თუ მომხმარებელი 5 ცდიდან ყველა სწორ მიმართულებას აირჩევს გამოიტანე
# “გამარჯვება” სხვა შემთხვევაში “შენ დამარცხდი”, თამაშის გამორთვა “exit” 