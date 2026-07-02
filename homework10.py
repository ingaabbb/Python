
# #1 შექმენი თამაში
# შექმენით Character კლასი (სახელი, სიცოცხლე, ძალა)
# გააკეთეთ მემკვიდრეები: Warrior, Mage, Archer
# გამოიყენეთ super() რომ მშობლის კონსტრუქტორი გამოიძახოთ
# თამაში: ორი გმირი ებრძვის ერთმანეთს (attack() მეთოდი).
# Warrior სჯობს Mage-ს , Mage სჯობს Archer-ს, Archer სჯობს Warrior-ს
# ტესტირების დროს სცადე სამივე ვარიანტი, ანუ როცა ერთმანეთზე გააკეთებინებ შეტევას 1 უნდა
# დამარცხდეს და 1მა გაიმარჯვოს, ეს უნდა გამოიტანო ტერმინალში. ზედმეტი ვალიდაციები და
# პირობის შეცვლა არაა საჭირო. რაც პირობაში წერია ამ მონახაზით გააკეთეთ თავისუფლად.
from dataclasses import dataclass

@dataclass
class Character:
    def __init__(self, name, live, power):
        self.name = name
        self.hp = hp
        self.power = power

    def attack(self, other):
        self_type = self.__class__.__name__
        other_type = other.__class__.__name__
    
        if (self_type == "Warrior" and other_type == "Mage") or (self_type == "Mage" and other_type == "Archer") or (self_type == "Archer" and other_type == "Warrior") :
            return (f"{self.name} won and {other.name} lose")
        else:
            return (f"{other.name} won and {self.name} lose")


class Warrior(Character):
    def __init__(self, name,hp, power):
        super().__init__(name, hp, power)


class Mage(Character):
    def __init__(self, name,hp, power):
        super().__init__(name, hp, power)

class Archer(Character):
    def __init__(self, name,hp, power):
        super().__init__(name, hp, power)     


Warrior1 = Warrior("warrior", 100, 5)
Mage1 = Mage("mage", 95, 10)
Archer1 = Archer("archer", 90, 10)
# print(Warrior1.attack(Mage1))
# print(Mage1.attack(Archer1))
# print(Archer1.attack(Mage1))
# print(Warrior1.attack(Archer1))

# #2 პატარა პროგრამა მონსტრებზე
# თქვენი ვალია შექმნათ მონსტრების ქარხანა სადაც:
# შექმენით Monster კლასი.
# დაამატეთ classmethod create_from_level(level), რომელიც ქმნის მონსტრს სიძლიერის
# მიხედვით.
# სხვადასხვა level -> სხვადასხვა ტიპის მონსტრი.
# შექმენი მინიმუმ 10 მონსტრი რომლებსაც ექნებათ სახელები, სახელები არ უნდა იყოს ბოროტული :)
# (ეს მონსტრები ეხმარებიან ადამიანებს) “აქაც იგივე” არაა საჭირო ზედმეტი ვალიდაციები და პირობის
# ცვლილება. ამ მონახაზში იმუშავეთ თავისუფლად.

class Monster:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    @classmethod
    def create_from_level(cls, name, level):
        if level == 1:
            monster_type = "მონსტრი"
        elif level == 2:
            monster_type = "მონსტრუნია"
        elif level == 3:
            monster_type = "მონსტრიკო"
        else:
            monster_type = "საყვარელი მონსტრი"
        return cls(name, monster_type)

    def __str__(self):
        return f"მონსტრის სახელია {self.name}, ტიპი : {self.type}"

monster1 = Monster.create_from_level("Mike Wazowski",2)
print(monster1)




# #3 მარტივი კაზინო თამაში

# შექმენით SlotMachine კლასი.
# გამოიყენეთ staticmethod შემთხვევითი სიმბოლოების დასაგენერირებლად.
# გამოიყენეთ classmethod from_difficulty(level) -> უფრო რთული დონის სლოტები
# მოთამაშე მოიგებს თუ სამივე სიმბოლო დაემთხვევა.

# აუცილებლად გატესტეთ, სცადეთ რამოდენიმე ვარიანტის გაშვება.
import random

class SlotMachine:

    def __init__(self, generated_symbols):
        self.generated_symbols = generated_symbols

    @staticmethod
    def random_symbols(symbols):
        our_symbols = random.choices(symbols, k=3)
        return our_symbols
    
    @classmethod 
    def from_difficulty(cls, level):

        if level == 1:
            symbols = ["#", "$"]
        elif level == 2:
            symbols = ["#", "$", "%"]
        elif level == 3:
            symbols = ["#", "$", "%", "&"]
        else:
            symbols = ["#", "$", "%", "&", "@"]

        return cls(symbols)
    
    def play(self):
        result = SlotMachine.random_symbols(self.generated_symbols)
        if len(set(result)) == 1:
            print(f"{result[0]}, {result[1]}, {result[2]} - გილოცავთ! მოიგეთ.")
        else:
            print(f"{result[0]}, {result[1]}, {result[2]} - სამწუხაროდ წააგეთ.")
            
my_game1 = SlotMachine.from_difficulty(1)
my_game1.play()

my_game1 = SlotMachine.from_difficulty(3)
my_game1.play()

my_game1 = SlotMachine.from_difficulty(5)
my_game1.play()


# #4 გმირის ქულების სისტემა
# შექმენით Hero კლასი.
# private health, private score.
# staticmethod random_event() -> შემთხვევითი მოვლენა (ქულა ემატება ან ჯანმრთელობა
# აკლდება).

# classmethod from_name(cls, name) -> ქმნის გმირს სახელით.
# მემკვიდრე SuperHero -> დამატებითი ძალა.
# super() გამოიძახეთ მშობლის კონსტრუქტორისთვის.
# თამაში გრძელდება სანამ გმირის health > 0.


        

# #5 პროგრამა კარტზე
# Card კლასი (rank, suit).
# Deck კლასი -> private cards list.
# classmethod create_standard_deck() აბრუნებს სტანდარტულ 52 კარტიან დასტას.
# staticmethod shuffle(cards) აურევს კარტებს.
# მოთამაშე იღებს 5 კარტს და ამოწმებს, აქვს თუ არა “მარტივი კომბინაცია” (მაგ: ორი ერთნაირი)
# აუცილებლად გატესტეთ კოდი, შეასრულეთ მხოლოდ პირობაში მოცემული ვარიანტი, არაა საჭირო
# დამატება.