# #1 მოცემულია სიტყვა "ABCD". დაბეჭდე ყველა შესაძლო ვარიანტი და **დაითვალე** რამდენია სულ რაოდენობრივად 
# (უნდა დააბრუნო რიცხვი)
# abcd abdc acbd acdb adbc adcb    bacd badc bcda dcad bdac bdca    cabd cadb cbad cbda cdba cdab   dabc dacb dbca dbac dcab dcba

import math, random, datetime
import itertools
from datetime import date, timedelta
word = "ABCD"

def possible_options(word):
    symbol = len(word) #4 
    number_of_options = math.factorial(symbol) #24
    print(f"სულ შესაძლო ვარიანტთა რაოდენობაა : {number_of_options}")

    word_list = list(word)
    options = itertools.permutations(word_list, symbol)

    list_possibles = []
    for i in options:
        possible_words = "".join(i)
        list_possibles.append(possible_words)
    return list_possibles
   
# print(possible_options(word))

# \#2 იპოვე მომდევნო კვირის პირველი სამშაბათი, საწყისი თარიღი არის დღევანდელი დღე (ხელით არ გაწეროთ თარიღი)

from datetime import date, timedelta

def find_Tuesday():
    today = date.today()
    today_weekday = today.strftime('%A') 

    Weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday", "Sunday"]

    count = 8
    for i in Weekdays:
        if i == today_weekday:
            day = today + timedelta(days=count)
        count -= 1

    return day



# \#3 დაადგინე, არის თუ არა შეყვანილი წელი ნაკიანი, მომხმარებელს შემოჰყავს მხოლოდ წელი და ვეუბნებით არის თუ არა ნაკიანი

# 1 ვარიანტი
import calendar


def check_leap (myinput):
    february = calendar.month(myinput, 2)

    my_day = date(myinput, 2, 28)

    check_day = my_day + timedelta(days = 1) 

    if check_day.strftime('%m') == "02":
        return(f"{myinput} ნაკიანი წელიწადია. ")
    else: 
        return(f"{myinput} არაა ნაკიანი წელიწადი")

# print(check_leap(2020))

# მეორე ვარიანტი:

def check_leap2(myinput):
    if calendar.isleap(myinput):
        print(f"{myinput} ნაკიანი წელიწადია. ")
    else: 
        print(f"{myinput} არაა ნაკიანი წელიწადი")


# \#4 დაითვალე რამდენი კვირაა დარჩენილი ახალ წლამდე, საწყისი თარიღი არის დღევანდელი დღე (ხელით არ გაწეროთ თარიღი)

today = date.today()
today_y = today.strftime('%Y')
today_d = today.strftime('%j')
print(today_d)

if calendar.isleap(int(today_y)):
    left_days = 366 - int(today_d)
else:
    left_days = 365 - int(today_d)

left_weeks = left_days // 7
print(f"ახალ წლამდე დარჩენილია {left_weeks} კვირა და {left_days % 7} დღე ")




# \#5 შექმენი ყველა 3-ელემენტიანი კომბინაცია სიიდან \[1,2,3,4,5] (itertools-ის გამოყენებით)

myList = [1,2,3,4,5]
options = itertools.combinations(myList, 3)
# for i in options:
#     print(i)


# options = itertools.permutations(myList,3)
# for k in options:
#     print(k)


# 6 მიიღე ყველა კომბინაცია "XYZ"-ის სიმბოლოებით სიგრძე 1-დან 3-მდე
# მაგალითი: X, Y, Z, XY, XZ, YZ, XYZ უნდა მივიღოთ მსგავსი შედეგი.


def combinations(word):
    word_len = len(word)  # 3

    t = 1
    combinations_list =[]
    while t < word_len + 1:
        options = itertools.permutations(word, t)
        for k in options:
            combinations_list.append("".join(k))
        t += 1

    return combinations_list

# print(combinations("XYZ"))



# \#7 თამაში უკუსვლაზე
# კომპიუტერი ირჩევს შემთხვევითობის პრინციპით რიცხვს 1-20 მდე, მოთამაშეს აქვს მხოლოდ 5 წამი რიცხვის გამოსაცნობად, 
# თუ 5 წამში სწორ რიცხვს ვერ შეიყვანს, თამაში სრულდება და გამოდის ტექსტი "დრო ამოიწურა, თქვენ დამარცხდით".

from datetime import datetime
# number = random.randint(1, 20)  
# start = datetime.now()   #ახლა
# start_seconds = start.strftime("%S")   # ახლა წამებში

# while datetime.now() < start + timedelta(seconds = 5):
#     guess_number = int(input("შემოიტანე რიცხვი"))
#     if guess_number == number and datetime.now() < start + timedelta(seconds = 5) :
#         print("ყოჩაღ, გამოიცანი!")
#         break
#     elif guess_number != number and datetime.now() < start + timedelta(seconds = 5):
#         print("არასწორია, სწრაფად სცადე თავიდან")
#     else:
#         print("სამწუხაროდ დრო ამოიწურა და დამარცხდით.")
#         break

# import inputimeout 
    



# \#8 ორი მოთამაშე იწყებს "გარბენს". უნდა შეამოწმო რომელი დაასრულებს ნაკლებ დროში
# start = datetime.now()

# player1_time = random.randint(5,20)
# player2_time = random.randint(5,20)

# player1 = start + timedelta(seconds=player1_time)
# player2 = start + timedelta(seconds=player2_time)

# print(f" პირველი: {player1}     მეორე: {player2}    ")

# if player1 < player2:
#     difference = player2_time - player1_time
#     print(f"პირველი მონაწილე უფრო სწრაფია. მან გარბენი დაასრულა {difference} წამით ნაკლებში")
# elif player1 == player2:
#     print(f"მონაწილეთა სისწრაფე ერთნაირია. გარბენი დაასრულეს {player1_time} წამში ")
# else:
#     difference = player1_time - player2_time
#     print(f"მეორე მონაწილე უფრო სწრაფია. მან გარბენი დაასრულა {difference} წამით ნაკლებში")




# \#9 იღბლიანი დაბადების დღე

# მოთამაშემ უნდა შეიყვანოს დაბადების თარიღი და თამაში დაითვლის რამდენი დღეა დარჩენილი შემდეგ დაბადების დღემდე
from datetime import date



# birthday = date(2000, 12, 10)

# def time_until_bd(birthday):
#     today = date.today()
#     today_d = int(datetime.today().strftime("%j"))
#     today_y = int(datetime.today().strftime("%Y"))

#     birthday_now = birthday.replace(year = today_y)  

#     if today < birthday_now:
#         days = int(birthday_now.strftime("%j")) - today_d

#     elif today > birthday_now:
#         find_birthday = birthday.replace(year = today_y + 1)

#         if calendar.isleap(today_y):
#             left_days = 366 - today_d
#         else:
#             left_days = 365 - today_d

#         days = left_days + int(find_birthday.strftime("%j"))
#     else:
#         days = 0

#     return f"დაბადების დღემდე დარჩენილია  {days} დღე"

# print(time_until_bd(birthday))






# \#10 საცავი - ჯუნიორ ჰაკერი :)

# თამაში არის შემდეგი - გვაქვს სეიფი რომელსაც აქვს ციფრები 1-6 მდე პაროლი არ ვიცით, ყოველ დღე კომპიუტერი აგენერირებს ახალ პაროლს
#  (შემთხვევითობის პრინციპით) პაროლი არის 4 ციფრიანი. ჩვენი მიზანია დავწეროთ ისეთი კოდი რომელიც შეამოწმებს ვარიანტებს და როცა მოხდება
#  კომპიუტერის მიერ დაგენერირებული პაროლის დამთხვევა უნდა გამოვიტანოთ შეტყობინება "პაროლი სწორია, საცავი გახსნილია", აუცილებელი
#  პირობაა გამოვიტანოთ ყველა ჩვენს მიერ ნაცადი პაროლი სანამ მივალთ სწორ ვარიანტამდე.

def real_password():
        
    sia =[]
    for i in range(4):
        sia.append(random.randint(1,6))
            
    sia_str = "".join(map(str, sia))
    number = int(sia_str)

    return number


print(real_password())


numbers = [1,2,3,4,5,6]
symbol = len(numbers) 

options = itertools.product(numbers, repeat=4)

for i in options:
    print("".join(map(str, i)))







# count = 1
# while True:

#     guess_password = input("დაწერეთ პაროლი")

#     if len(guess_password) != 4 or not guess_password.isdigit():
#         print("დაწერეთ მხოლოდ ოთხნიშნა რიცხვი")

#     else:
#         if number == int(guess_password):
#             print("პაროლი სწორია, საცავი გახსნილია")
#             break
#         else:
#             print(f" ჩენ მიერ {count} მცდელობისას შეყვანილი პაროლი {guess_password} არასწორია, სცადე ხელახლა.")
#             count +=1 





    






# სავარჯიშოები გავყოთ ორ ნაწილად: 1-6 მდე სავარჯიშოებისთვის გავაკეთოთ ახალი ბრანჩი რომელსაც დავარქმევთ სახელს და ვიმუშავებთ, 
# როდესაც დავასრულებთ ყველას უნდა მოხდეს GITHUB-ზე ატანა გიტ ბრძანებებით. 7-10-მდე სავარჯიშოებისთვის უნდა გავაკეთოთ კიდევ ერთი
# ბრენჩი და იქ ვიმუშაოთ, დასრულების შემდეგ ავიტანოთ GITHUB-ზე, გავაკეთოთ ყველას MERGE და ამის შემდეგ განვაახლოთ ჩვენი main ბრენჩი EDITOR-ში.

# ყველა ბრძანება ამოიწერეთ და დავალებას დაურთეთ თან, ასევე მიუთითეთ თქვენი გითჰაბის შესაბამისი რეპოზიტორია.