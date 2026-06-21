# #1 unittest1

# შექმენით Calculator კლასი add, subtract, multiply, divide მეთოდებით. დაწერეთ unittest რომელიც ამოწმებს ყველა მეთოდს.
# გაითვალისწინეთ 0-ზე გაყოფაც.
# გამოიყენეთ unittest მოდული
# გამოიყენეთ setup მეთოდი.

class Calculator:
    def divide (self, a,b):
        if b == 0:
            raise ValueError("ნულზე გაყოფა არ შეიძლება!")
        return a / b
    
    def add (self, a,b):
        return a + b
    def multiply(self, a,b):
        return a * b
    def subtract (self, a,b):
        return a-b

import unittest

class Mytest(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator() # ყოველ ჯერზე ქმნის ახალ კალკულატორს ანუ ამზადებს გარემოს ტესტირებისთვის

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2,5),10)
        self.assertEqual(self.calc.multiply(2,25),50)
        self.assertEqual(self.calc.multiply(22,11),242)

    def test_divide(self):
        self.assertEqual(self.calc.divide(40,2),20)
        self.assertEqual(self.calc.divide(250,2),125)
        self.assertEqual(self.calc.divide(42,6),7)
    
    def test_add(self):
        self.assertEqual(self.calc.add(5,7),12)
        self.assertEqual(self.calc.add(22,5),27)
        self.assertEqual(self.calc.add(11,9),20)
    
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(20,5),15)
        self.assertEqual(self.calc.subtract(47,5),42)
        self.assertEqual(self.calc.subtract(99,2),97)

if __name__ == '__main__':

    unittest.main()

# #2 unittest2

# შექმენით BankAccount კლასი deposit და withdraw მეთოდებით. დაწერეთ unittest რომელიც ამოწმებს:
# - სწორი ბალანსი

# - უარყოფითი თანხის შეტანისას შეცდომა

# - თანხის გამოტანა ბალანსზე მეტისას შეცდომა

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        if amount <=0:
            raise ValueError("უარყოფით თანხას ვერ შეიტანთ")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("ამდენი თანხა არ არის ანგარიშზე")
        elif amount <= 0:
            raise ValueError("გამოსატანი თანხა უნდა იყოს დადებითი")
        self.balance -= amount
        return self.balance 

class my_test(unittest.TestCase):
    def setUp(self):
        self.BankAcc = BankAccount(balance=100)

    def test_deposit(self):
        self.assertEqual(self.BankAcc.deposit(5),105)
        with self.assertRaises(ValueError):
            self.BankAcc.deposit(-20)
    
    def test_withdraw(self):
        self.assertEqual(self.BankAcc.withdraw(10),90)
        with self.assertRaises(ValueError):
            self.BankAcc.withdraw(120)


if __name__ == '__main__':
    unittest.main()

# #3 unittest3

# შექმენით ფუნქცია რომელიც იღებს JSON (dict) response-ს და აბრუნებს "status"-ის მნიშვნელობას. თუ status არ არსებობს → შეცდომა. 
# დაწერეთ ტესტები

def function(response):
    count = 0
    if "status" in response:
        return response["status"]
    else:
        raise KeyError("სიაში არ არსებობს status")
    
class test_response(unittest.TestCase):

    def test_function(self):
        dict1 = {"status": "haha", "lala" : "la1"}
        dict2 = {"Hah": 12 , "lala": 34}
        self.assertEqual(function(dict1), "haha")
        with self.assertRaises(KeyError):
            function(dict2)

if __name__ == '__main__':
    unittest.main()
    
        

