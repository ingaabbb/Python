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







    






# სავარჯიშოები გავყოთ ორ ნაწილად: 1-6 მდე სავარჯიშოებისთვის გავაკეთოთ ახალი ბრანჩი რომელსაც დავარქმევთ სახელს და ვიმუშავებთ, 
# როდესაც დავასრულებთ ყველას უნდა მოხდეს GITHUB-ზე ატანა გიტ ბრძანებებით. 7-10-მდე სავარჯიშოებისთვის უნდა გავაკეთოთ კიდევ ერთი
# ბრენჩი და იქ ვიმუშაოთ, დასრულების შემდეგ ავიტანოთ GITHUB-ზე, გავაკეთოთ ყველას MERGE და ამის შემდეგ განვაახლოთ ჩვენი main ბრენჩი EDITOR-ში.

# ყველა ბრძანება ამოიწერეთ და დავალებას დაურთეთ თან, ასევე მიუთითეთ თქვენი გითჰაბის შესაბამისი რეპოზიტორია.