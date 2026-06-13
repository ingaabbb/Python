# #1 ამოცანა 1
# შექმენი კლასი BankAccount, რომელსაც ექნება:
# დახურული ატრიბუტები: __balance, __owner.
# მეთოდი deposit(amount) – თანხის დამატება.
# მეთოდი withdraw(amount) – თანხის გამოტანა (არ უნდა გადავიდეს მინუსში).
# მეთოდი get_balance() – მხოლოდ წაკითხვისთვის.
# დაწერე კოდი ისე, რომ მომხმარებელს პირდაპირ __balance-ზე წვდომა არ ჰქონდეს.

class BankAccount:
    def __init__(self, owner, balance):
        self.__owner = owner
        self.__balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("თანხა უნდა იყოს დადებითი")
    def withdraw(self, amount):
        if self.__balance - amount > 0:
            self.__balance -= amount
        else:
            print("შეცდომაა, ანგარიშზე არ არის საკმარისი თანხა")
    def get_balance(self):
        return self.__balance 
        
    

# #2 ამოცანა 2
# შექმენი კლასი ShoppingCart, რომელსაც ექნება:
# ატრიბუტი items (სიაში პროდუქტების რაოდენობა).
# __len__() დააბრუნებს პროდუქტების რაოდენობას.
# __eq__() ორი კალათის შედარება – აბრუნებს True, თუ რაოდენობა ტოლია.

# გააკეთე 2 კალათა და შეადარე.
# გააკეთე 3 კალათა და შეადარე.
# გააკეთე 4 კალათა და შეადარე.

class ShoppingCart:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return f"სიაში პროდუქტების რაოდენობაა {len(self.items)}"
        
    def __eq__(self, other):
        return len(self.items) == len(other.items)
        
        
items1 = ShoppingCart(["მაისური", "ჯინსი"])
items2 = ShoppingCart(["მაისური", "ფეხსაცმელი", "ჯინსი"])
items3 = ShoppingCart(["მაისური", "ფეხსაცმელი", "ქურთუკი"])
items4 = ShoppingCart(["ფეხსაცმელი", "ჯინსი"])

print(items2 == items3)

# #3 ამოცანა 3
# გამოიყენე @dataclass მოდული კლასის Book შესაქმნელად:
# ველები: title, author, year.
# დაამატე მეთოდი is_classic() → აბრუნებს True, თუ წელი < 1970.
# შექმენი რამდენიმე წიგნი და შეამოწმე ფუნქცია.

from dataclasses import dataclass

@dataclass
class Book:
    title : str
    author : str
    year : int

    def is_classic(self):
        if self.year < 1970:
            return True
        else:
            return False
        

Book1 = Book("Animal Farm", "George Orwell", 1945)
Book2 = Book("Metamorphosis", "Franz Kafka", 1915)
Book3 = Book("ანტონიო და დავითი", "ჯემალ ქარჩხაძე", 1987)

print(f"{Book1.title} is classic.  -  {Book1.is_classic()}")


# #4 ამოცანა 4
# შექმენი კლასი Person, რომელსაც ექნება __del__() მეთოდი, რომელიც ბეჭდავს "Person removed" როცა ობიექტი წაიშლება.
# შექმენი ობიექტი, შემდეგ წაშალე del-ით და ნახე როგორ რეაგირებს garbage collector.

class Person:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print("Person removed")
        
Person1 = Person("Mariam")
print(Person1.name)
del Person1


# #5 ამოცანა 5
# შექმენი კლასი Temperature, რომელსაც ექნება:
# დახურული ატრიბუტი __celsius.
# get და set property °C-სთვის.
# fahrenheit property (read-only), რომელიც აბრუნებს °F.
# შექმენი ობიექტი, შეცვალე °C და შეამოწმე °F ავტომატურად იცვლება თუ არა.

class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius

    @property
    def celsius (self):
        return self.__celsius


    @celsius.setter
    def celsius(self, value):
        self.__celsius = value

    @property
    def fahrenheit(self):
        return (self.__celsius * 9/5) + 32
    
temperature1 = Temperature(30)
print(temperature1.celsius)
temperature1.celsius = 20
print(temperature1.celsius)
print(temperature1.fahrenheit)


# #6 ამოცანა 6
# შექმენი კლასი CustomList, რომელიც:
# ინახავს ელემენტებს.
# __getitem__() – აბრუნებს ელემენტს ინდექსით.
# __setitem__() – ცვლის ელემენტს.
# __iter__() – Iterable უნდა იყოს.
# გამოიყენე for ციკლში შენი CustomList.

class CustomList:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, key):
        return self.items[key] 
    
    def __setitem__(self, key, value):
        self.items[key] = value

    def __iter__(self):
        return iter(self.items)
    
list1 = CustomList(["ერთი", "ორი", "სამი", "ოთხი"])
print(list1[1])

list1[1] = "ხუთი"
print(list1[1])


for i in list1:
    print(i)


# #7 ამოცანა 7
# შექმენი კლასი Refrigerator, რომელსაც ექნება:
# ატრიბუტი items (სია).
# __contains__() – აბრუნებს True, თუ პროდუქტი მაცივარშია ("milk" in fridge).
# __str__() – "Fridge with N items".
# __del__() – "Fridge unplugged!".
# დაამატე პროდუქტები, შეამოწმე "milk" in fridge, დაბეჭდე ობიექტი და ბოლოს წაშალე.

class Refrigerator:
    def __init__(self, items):
        self.items = items

    def __contains__(self, value):
        if value in self.items:
            return True
        else: 
            return False
    
    def __str__(self):
        return f"Fridge with  {len(self.items)} items."

    def __del__(self):
        print ("Fridge unplugged!")

Fridge = Refrigerator(["apple" , "milk", "meat"])
print("milk" in Fridge)


# #8 ამოცანა 8
# შექმენი კლასი FunnyCalculator, რომელსაც ექნება:
# __add__() – აბრუნებს "Why are you adding numbers? Just buy a calculator".
# __mul__() – აბრუნებს "Multiplication is too mainstream...".
# __truediv__() – თუ გაყოფ 0-ზე, ბეჭდავს "ZeroDivisionError? Nah, let’s just say infinity"
# __str__() – "I’m the funniest calculator in Python!".
# ცადე calc + 5, calc * 2, 10 / calc და ნახე რა მოხდება.

class FunnyCalculator:
    def __init__(self):
        pass
    def __add__(self, other):
        return "Why are you adding numbers? Just buy a calculator. "
    def __mul__(self, other):
        return "multiplication is too mainstream..."
    def __truediv__(self, other):
        if other == 0:
            return "ZeroDivisionError? Nah, let’s just say infinity"
        else:
            return "regular division"
    def __str__(self):
        return "I’m the funniest calculator in Python!"
    
calculator = FunnyCalculator()
print(calculator)
print(calculator + 5)
print(calculator * 2)
print(10/ calculator)
