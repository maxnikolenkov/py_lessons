#Показать здоровье, деньги и урон
def show_health(hp):
    print(f"Здоровье: {hp}")
def show_money(money):
    print(f"Деньги: {money}")
def show_damage(damage):
    print(f"Сила: {damage}")

#Герой
hp = 100
money = 500
damag = 10


#Лечение и получение урона(когда ударили)
def hear(hp):
    hp = hp + 10
    return hp
def damage(hp):
    hp = hp - 15
    return hp
    
    
#Главное меню
while True:
    print("1 - Показать здоровье")
    print("2 - Показать деньги")
    print("3 - Показать сила")
    print("4 - Мини бой")
    print("5 - Выход")
    choice = int(input("Ваш выбор: "))
    if choice == 1:
        show_health(hp)
    if choice == 2:
        show_money(money)
    if choice == 3:
        show_damage(damag)
    if choice == 4:
        print("1 - Лечение")
        print("2 - Нас ударили")
        battle_choice = int(input("Ваш выбор: "))
        if battle_choice == 1:
           print(f"Ваша жизнь: {hear(hp)}")
        if battle_choice == 2:
           print(f"Ваша жизнь: {damage(hp)}")
            

        
    if choice == 5:
        break


