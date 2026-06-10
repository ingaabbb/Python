# #1 SQL დავალება
# გამოიტანე ProductName, CategoryID, Unit, Price ცხრილი- “პროდუქტები”

# სადაც ფასი მოთავსებული 18-სა და 25-ს შორის
# დაალაგე კლებადობით ფასის მიხედვით

# SELECT ProductName, CategoryID, Unit, Price FROM Products
# WHERE Price BETWEEN 18 AND 25 
# ORDER BY Price DESC


# #2 SQL დავალება2
# გამოიტანე ყველა ველი, სადაც რაოდენობა ტოლია 15-ის ან 12-ის
# დაალაგე ზრდადობით
# ცხრილი - “OrderDetails”

# SELECT * FROM OrderDetails
# WHERE  Quantity=15 OR Quantity=12
# ORDER BY Quantity


# #3 მოცემულია JSON მასივი:
# [
# {"id": 1, "price": 50},
# {"id": 2, "price": 200},
# {"id": 3, "price": 150}
# ]
# ამოიღე მხოლოდ ის პროდუქტები, რომელთა ფასი 100-ზე მეტია.

products = [
  {"id": 1, "price": 50},
  {"id": 2, "price": 200},
  {"id": 3, "price": 150}
]

for i in products:
    if i["price"] > 100 :
        print(i)


# with open(file = "products.json", Opentextmode= 'w', encoding="utf-8", ) as file:
#     products_list = [ {"id": 1, "price": 50},{"id": 2, "price": 200},{"id": 3, "price": 150}]

#     json.dump(products_list, file, indent=4)

# with open(file="products.json", opentextmode= 'r', ) as file:
#     products = json.load(file)

    
#     for i in products:
#         if i["price"] > 100 :
        

# #4 მოცემულია რთული JSON:


monacemebi= {
"company": {
        "departments": [
                        {"name": "IT", "employees": [{"name": "Ana"}, 
                                                     {"name": "Beka"}]},

                        {"name": "HR", "employees": [{"name": "Nino"}]}
                        ]
}
}
# ამოიღე ყველა თანამშრომლის სახელი
departamentebi= monacemebi["company"]["departments"]
print(departamentebi)
for i in departamentebi:
    for k in i["employees"]:
        print(k["name"])


# #5 მოცემულია სტუდენტების სია:
studentebi= [
{"name": "Ana", "grades": [90, 80, 95]},
{"name": "Beka", "grades": [70, 85, 88]},
{"name": "Nino", "grades": [100, 95, 99]}
]

# იპოვე სტუდენტი, რომელსაც აქვს საშუალო ქულის მიხედვით საუკეთესო
# შედეგი.
max = 0 
jami = 0
sauketeso_studenti = None
for i in studentebi:
    saxeli = i["name"] 
    qula = i["grades"]
    for k in i["grades"]:
        jami += k
    sashualo = jami/ len(i["grades"])

    if max < sashualo:
        max = sashualo
        sauketeso_studenti = i["name"]
    jami = 0
        
# print(f"{sauketeso_studenti}  hqonda sauketeso shedegi - {max}")


# #6 მოცემულია კომპანიების სია:
monacemebi = {
"companies": [
{
    "name": "TechCorp", "employees": [
                        {"name": "Ana", "salary": 3000},
                        {"name": "Beka", "salary": 4500}
                        ]
},
{
    "name": "SoftPlus", "employees": [
                        {"name": "Nino", "salary": 5000},
                        {"name": "Giorgi", "salary": 2500}
                        ]
}
]
}
# იპოვე ყველა თანამშრომელი, რომლის ხელფასი მეტია 4000-ზე და დაბეჭდე
# მათი სახელები + კომპანიის სახელი.

# companiebi = monacemebi["companies"]
# for i in companiebi: 
#     tanamshromlebi = i["employees"]
#     for k in tanamshromlebi:
#         if k["salary"] > 4000:
#             print(f' {k["name"]} ის ხელფასი მეტია 4000 ზე. ის მუშაობს {i["name"]} ')




import requests

# #7 გააგზავნე GET მოთხოვნა https://jsonplaceholder.typicode.com/users და
# დაბეჭდე პირველი მომხმარებლის სახელი.

motxovna = requests.get("https://jsonplaceholder.typicode.com/users")
sia = motxovna.json()

pirveli_momxmarebeli = sia[0]["name"]    
# print(pirveli_momxmarebeli)



# #8 გააგზავნე POST მოთხოვნა https://jsonplaceholder.typicode.com/posts და
# შექმენი ახალი პოსტი შემდეგი მონაცემებით:
# {"title": "Test", "body": "Hello World", "userId": 5}

monacemebi = {
    "title": "Test", "body": "Hello World", "userId": 5
}

my_post = requests.post("https://jsonplaceholder.typicode.com/posts", json=monacemebi)

# print(my_post.json())

# #9 წამოიღე ყველა TODO task და დაბეჭდე მხოლოდ ის, სადაც "completed": False -
# https://jsonplaceholder.typicode.com/todos
# ბოლოს დათვალე რამდენი შეუსრულებელი ტასკია (რაოდენობაში)

# motxovna = requests.get("https://jsonplaceholder.typicode.com/todos")
# sia = motxovna.json()
# count = 0
# for i in sia:
#     if i["completed"] == False:
#         print(i["title"])
#         count += 1

# print(f" სულ შეუსრულებელი დავალებაა {count}")


# #10 ამოიღე ყველა პოსტი https://jsonplaceholder.typicode.com/posts, შემდეგ
# იპოვე ავტორის სახელი (users API-დან) და დაბეჭდე:
# "Post Title – Author Name"
# გამოიტანე მხოლოდ პირველი 5

postebi = requests.get("https://jsonplaceholder.typicode.com/posts").json()
avtori = requests.get("https://jsonplaceholder.typicode.com/users").json()

count = 0
for i in postebi:
    for k in avtori:
        if k["id"] == i["userId"]:
            print(f'{i["title"]} - {k["name"]}')
    count += 1
    if count == 4: break

# დავალება დაწერეთ 1 ფაილში და ისე ატვირთეთ Classroom-ში
# ბაზებისთვის გამოიყენეთ: https://www.w3schools.com/sql/trysql.asp?filename=trysql_editor