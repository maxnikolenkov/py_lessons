def hello():
    return "Привет!"
print(hello())
"""1 Вариант"""
#def hello_user():
#    name = input("Введите ваше имя:")
#    return "Привет," + name
#print(hello_user())
"""2 Вариант"""
#def hello_user(user):
#    return "Привет," + user
#user0 = input("Введите ваше имя:")
#print(hello_user(user0))

def add_number(a,b):
    return a + b
s = add_number(8,7)
print(f"Сумма 8 и 7 равна {s}")
"""Калькулятор Корзины"""
def calc_total(price, quantity):
    return price * quantity
def apply_discount(subtotal, sale):
    n = subtotal - (subtotal * (sale/100))
    return n
def add_tax(summa, tax=0.20):
    t = summa + (summa * tax)
    return t
def format(value):
    return(f"Итого: {round(value, 2)}")
def process_orde(price, quantity, sale):
    a = calc_total(price, quantity)
    b = apply_discount(a, sale)
    c = add_tax(b, 0.22)
    return print(format(c))
process_orde(100, 10, 10)
def bears():
    a = 10
    return a
def eagle():
    b = 150
    return b
def e_animals(a,b):
    return (f"Всего у нас {a+b} редких животных")
print(bears())
print(eagle())
print(e_animals(bears(), eagle()))
    


