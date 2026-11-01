from random import randint
#Показать здоровье, деньги и урон
def show_health(hp):
    print(f"Здоровье: {hp}")
def show_money(money):
    print(f"Деньги: {money}")
def show_damage(damage):
    print(f"Сила: {damage}")

def enemy():
    enemies = randint(1,3)
    if enemies == 1:
        return "Слизень", 20, 5, randint(5,10)
    elif enemies == 2:
        return "Гоблен", 35, 8, randint(10,20)
    elif enemies == 3:
        return "Скелет", 50, 12, randint(20,35)
def attack_enemy(player_damage, emeny_hp):
    enemy_hp = enemy_hp - player_damage
    print(f"Вы нанесли {player_damage} урона")
    print(f"Осталось здоровья у врага: {enemy_hp}")
    return enemy_hp
def attack_player(enemy_damage, player_hp):
    player_hp = player_hp - enemy_damage
    print(f"Вам нанесли {enemy_damage} урона")
    return player_hp
#Герой
hp = 100
money = 500
damag = 10


#Лечение 
def hear(player_hp, player_gold):
    if player_gold >= 10:
        player_gold = player_gold - 10
        player_hp = player_hp + 25
        if player_hp > 100:
            player_hp = 100
        print("Вы выпили зелье")
        print("Вы востановили 25 здоровья")
    else:
        print("Недостаточно золота")
    return player_hp, player_gold
def battle(player_hp, player_damage, player_gold):
    enemy_name, enemy_hp, enemy_damage, enemy_gold = enemy()
    print()
    print(f"Появился {enemy_name}!")
    print()
    while enemy_hp > 0 and player_hp > 0:
        enemy_hp = attack_enemy(player_damage, enemy_hp)
        if enemy_hp <= 0:
            print()
            print(f"{enemy_name} побежден")
            print(f"Вы получили {enemy_gold} золота!")
            player_gold = player_gold + enemy_gold
            break
        print(f"{enemy_name} Здоровье: {enemy_hp}")
        player_hp = attack_enemy(player_hp, enemy_hp)

        if player_hp <= 0:
            print("Вы проиграли")
            break
        print(f"Ваше здорорвье: {player_hp}")
        return player_hp, player_gold 

    
    
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
        hp, money = battle(hp, damag, money)


        
    if choice == 5:
        break


