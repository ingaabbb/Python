# #4 pytest1
# შექმენით ფუნქცია Celsius → Fahrenheit. დაწერეთ pytest ტესტები approx-ის გამოყენებით.
# ნიმუში: assert pytest.approx
import pytest

def Celsius_change(value):
    value_f = value*1.8+32
    return value_f

def test_degrees():
    assert Celsius_change(5) == pytest.approx(41)
    assert Celsius_change(6) == pytest.approx(41)



# #5 pytest2

# შექმენით ფუნქცია რომელიც ამოწმებს მომხმარებლის ლოგინს და პაროლს dictionary-დან
# pytest-ში გამოიყენეთ raises შეცდომის დასატესტად

# ნიმუში: raise ValueError
def check_acc(data, email, password):
    if email not in data:
        raise KeyError("მეილი არასწორია")
    
    if data[email] != password:
        raise ValueError("პაროლი არასწორია")
    return True

dict1 = {"abc@mail.ge" : "1234!" , "def@mail.ge": "5678%"}
    
def test_acc():
    assert check_acc(dict1, "abc@mail.ge", "1234!") == True

    with pytest.raises(ValueError):
        check_acc(dict1, "abc@mail.ge", "432")

    with pytest.raises(KeyError):
        check_acc(dict1, "abcde@mail.ge", "432")    


         
# #6 pytest3

# დაწერეთ ფუნქცია, რომელიც ამოწმებს არის თუ არა სტრიქონი სწორი email (ანუ შეიცავს @ და . სიმბოლოებს)
# pytest-ით გააკეთეთ ტესტები parametrization-ის გამოყენებით

# ნიმუში: @pytest.mark.parametrize

def check_email(email):
    if "@" in email and "."in email:
        return True
    else:
        return False

@pytest.mark.parametrize("input, result", [("abc@mail.ge", True), ("user@gm.com", True), ("abc@mail", False), ("abdc.", False)])

def test_email_validation(input, result):
    assert check_email(input) == result
