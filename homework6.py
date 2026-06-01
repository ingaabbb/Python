

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

numbers = "123456"

def possible_options(word):
    
    sia =[]
    for i in range(4):
        sia.append(random.randint(1,6))

    for k in sia:
        str_number += str(k)

    number = int(str_number)
    






    






# სავარჯიშოები გავყოთ ორ ნაწილად: 1-6 მდე სავარჯიშოებისთვის გავაკეთოთ ახალი ბრანჩი რომელსაც დავარქმევთ სახელს და ვიმუშავებთ, 
# როდესაც დავასრულებთ ყველას უნდა მოხდეს GITHUB-ზე ატანა გიტ ბრძანებებით. 7-10-მდე სავარჯიშოებისთვის უნდა გავაკეთოთ კიდევ ერთი
# ბრენჩი და იქ ვიმუშაოთ, დასრულების შემდეგ ავიტანოთ GITHUB-ზე, გავაკეთოთ ყველას MERGE და ამის შემდეგ განვაახლოთ ჩვენი main ბრენჩი EDITOR-ში.

# ყველა ბრძანება ამოიწერეთ და დავალებას დაურთეთ თან, ასევე მიუთითეთ თქვენი გითჰაბის შესაბამისი რეპოზიტორია.