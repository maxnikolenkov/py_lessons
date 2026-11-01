fruts = ["Яблолко", "Банан", "Апельсин", "Манго", "Мандарин"]
"""
print(fruts[0])
print(fruts[1])
print(fruts[2])
print(fruts[3])
print(fruts[4])
Можно заменить на:
"""
for i in range(5):  #Для каждой i будет подбираться число от 0 до 4
    print(fruts[i])

ice_creem = {"Ваниль":10, "Шоколад":10, "Клубничное":2}
#print("Количество Ванили:")
#print(ice_creem["Ваниль"])
while True:
    choice = str(input("Какой вкус вы хотите?\n"))
    print(f"Количество {choice}")
    print(ice_creem[choice])
    if ice_creem[choice] > 0:
        print("Вот ваше мороженое")
        ice_creem[choice] = ice_creem[choice] - 1
    else:
        print("Простите, такой вкус кончился")
        print("Хотите добавить вкус или количество в наш магазин?")
        answer = str(input("Да или Нет"))
        if answer == "Да":
            taste = str(input("Введите вкус:\n"))
            n = int(input("Введите количество:\n"))
            ice_creem[taste] = n
            print(f"Теперь у нас есть: {ice_creem}")
        else:
            break
        
"""
class_list = {"Саша":3, "Максим":2, "Маша":1, "Антон":1, "Артём":2}
print(class_list)
for i in class_list:
    print(i, end = ": ")
    print(class_list[i])
"""    
        

