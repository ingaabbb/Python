# #1 შექმენი გენერატორი, რომელიც ტექსტის თითოეულ სიმბოლოს აბრუნებს.
Word = "CODE"

def my_gen(word):
    for i in word:
        yield i

gen = my_gen(Word)

for i in range(len(Word)):
    print(next(gen))



# #2 დაწერე პროგრამა რომელშიც მომხმარებელი შემოიყვანს მხოლოდ ციფრებს, ლოგიკა
# უნდა იყოს შემდეგი: გვაქვს კონკრეტული ლისტი და მომხმარებელი უნდა მიწვდეს
# შემოყვანილი ციფრით რომელიმე ელემენტს, თუ ვერ მიწვდება პროგრამა შეცდომაზე არ
# უნდა გავიდეს.
# arr = [1, 2, 3,4,5,6,7,8,9]

# while True:
#     try:
#         user_input = input("შემოიყვანეთ ციფრი")
#         user_input_int = int(user_input)

#         chosen_number = arr[user_input_int-1]

#         print(f"თქვენ მიერ  არჩეული ციფრია: {chosen_number}")
#         break
#     except IndexError:
#         print("ამ ნომრით ელემენტი არ არსებობს სიაში")

#     except ValueError:
#         print("შეიყვანეთ მხოლოდ ციფრები")


# #3 შექმენი დეკორატორი, რომელიც ითვლის რამდენჯერ გამოიძახეს ფუნქცია.
# მაგალითი:
# @counter
# def say():
# print("Hi")
# say()
# say()
# გამოძახება: 1
# Hi
# გამოძახება: 2
# Hi

def counter(function):
    count = 0
    def wrapper(*args,**kwargs):
        nonlocal count 
        count += 1
        print(f"ფუნქცია გამოიძახეს {count}-ჯერ")
        result = function(*args,**kwargs)
        return result
    return wrapper

@counter
def myfunc():
    return "Hi"


# print(myfunc())
# print(myfunc())


# #4 მომხმარებელს უნდა დავუსვათ 5 მათემატიკური შეკითხვა, თითოეულზე სწორი
# პასუხი არის 10 ქულა ხოლო არასწორი 0 ქულა, მიღებული პასუხებიდან უნდა
# განვსაზღვროთ რამდენი ქულა აიღო მომხმარებელმა, შევქმნათ ლოფ ფაილი
# game.log და შევინახოთ ყველა ქულა. ბოლოს გამოვუტანოთ მიღებული შედეგი
import logging 

# logging.basicConfig(
#     filename = "game.log",
#     level = logging.INFO,
#     format='%(asctime)s - %(levelname)s - %(message)s',
#     encoding='utf-8'
# )

# questions_answers={"რას უდრის 6*8": 48 ,
#                 "რამდენია 95/5" : 19, 
#                 "რას უდრის 8-ის კვადრატი": 64, 
#                 "რა არის 2x-ის წარმოებული?" : 2, 
#                 "რამდენია 7-2": 5}

# count = 0
# scores = 0
# for i, k in questions_answers.items():

#     print(f" შეკითხვა {count + 1}: {i}")
#     answer = int(input("დაწერე პასუხი"))
#     if answer == k:
#         scores += 10 
#         print(f"ყოჩაღ, შენი ქულაა: {scores}")
#         logging.info(f" {count+1} შეკითხვაზე პასუხი სწორია.  ქულა: {scores}")
#     else:
#         print(f"შეცდომაა, შენი ქულა იგივე დარჩა: {scores}")
#         logging.info(f" {count +1} შეკითხვაზე პასუხი არასწორია. მიმდინარე ქულა: {scores}")
#     count +=1

# print(f"ქვიზი დასრულდა! შენი ქულაა: {scores}")
# logging.info(f"ქვიზი დასრულდა. საბოლოო ქულა: {scores}")




# #5 შექმენით ფაილი quiz.log, შექმენით გენერატორი რომელშიც შენახული იქნება
# 5 შეკითხვა და სათითაოდ დააბრუნებს, მომხმარებელმა უნდა უპასუხოს ყველა
# შეკითხვას და პასუხები შეინახეთ ლოგ ფაილში.

# logging.basicConfig(
#     filename = "quiz.log",
#     level = logging.INFO,
#     format='%(asctime)s - %(levelname)s - %(message)s',
#     encoding='utf-8'
# )

# def questions_generator(questions_list):
#     for i in questions_list:
#         yield i

# questions = ["რა გქვიათ?",
#             "რამდენი წლის ხართ?" ,
#             "რომელია თქვენი საყვარელი წელიწადის დრო?",
#             "რომელია თქვენი საყვარელი დესერტი?",
#             "ხაჭაპური გირჩევნიათ თუ ლობიანი?" ]

# gen = questions_generator(questions)
# count = 0
# for i in range(len(questions)):
#     print(next(gen))
#     answer = input("დაწერეთ პასუხი")
#     logging.info(f"{questions[count]} შეკითხვაზე პასუხია: {answer}")
#     count +=1 


# #6 შექმენი პროგრამა სადაც მომხმარებელი ეჯიბრება კომპიუტერს: ქვა/ბადე/
# მაკრატელის თამაშში, თამაში არის სამამდე, კომპიუტერი შემთხვევითობის
# პრინციპით ირჩევს ამ სამიდან 1-ს , ასევე ტერმინალში მომხმარებელი წერს ერთ-
# ერთს, ერთნაირის შემთხვევაში ფრეა და გრძელდება თამაში 3-მდე, ვინც პირველი

# მიაღწევს 3-ს გამოიტანე შეტყობინება .....-მ გაიმარჯვა, ყველა ნათამაშები ხელი
# უნდა შეინახოო ლოგირების ფაილში.
import random

logging.basicConfig(
    filename = "RockPaperScissors.log",
    level = logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)
options = ["rock", "paper", "scissors"]
user_score = 0
computer_score=0
count =1

while computer_score < 3 and user_score < 3:
    computer_choice= random.choice(options)
    user_choice = input("choose : rock, paper or scissors")

    print(f"your choice: {user_choice}, computer choice: {computer_choice}")
    logging.info(f" {count} try - user choice: {user_choice}, computer choice: {computer_choice}")

    if (computer_choice == "scissors" and user_choice == "paper") or (computer_choice == "rock" and user_choice == "scissors" ) or (computer_choice == "paper" and user_choice == "rock"):
        computer_score += 1

    elif computer_choice == user_choice:
        print("ორივეს არჩევანი დაემთხვა")
    else:
        user_score +=1

    print(f"after {count} try - scores: computer:{computer_score},  your:{user_score} ")
    logging.info(f"scores: computer:{computer_score},  your:{user_score}")
    count += 1

if user_score == 3:
    print("good job, you won")
    logging.info("user won")
else:
    print("Sadly, you lose")
    logging.info("computer won")






# #7 პროგრამა კამათელზე - გვყავს ორი მომხმარებელი Gamer 1 & Gamer 2,
# თითოეულს უნდა გავაგორებინოთ კამათელი თითო თითოჯერ, თუ ფრეა ვიმეორებთ,
# სხვა შემთხვევაში მოგებულ მოთამაშეს უნდა ვკითხოთ კიდევ 1 შანსს მისცემს თუ
# არა წაგებულს და კიდევ გააგორებს თუ არა, თუ უარია ვამთავრებთ, თუ თანახმაა
# იგივე ლოგიკა უნდა გაგრძელდეს სანამ უარს არ იტყვის ერთ-ერთი.


# #8 შექმენი პროგრამა სადაც გექნება გადაცემული 10 სიტყვა ლისტში და ლოგიკა
# არის შემდეგი, ამ სიტყვებიდან 2 ცალს ირჩევ შემთხვევითობის პრინციპით და
# თითოეული სიტყვიდან უნდა ამოაკლო 2 ასო და მომხმარებელს აჩვენო მსგავსი
# ფორმით და უთხრა რომ გამოიცნოს სიტყვა და ჩაწეროს სრულად, თუ გამოიცნო
# “გამარჯვება” თუ ვერ გამოიცნო ვერცერთი სიტყვა “დამარცხდი”, ერთის
# გამოცნობის შემთხვევაში “50%”

# დავალება მოამზადეთ მხოლოდ 1 ფაილში და ისე ატვირთეთ, გამოიყენეთ PEP8
# სტანდარტი და მიჰყევით მხოლოდ ამოცანის პირობას.