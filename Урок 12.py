#ice_cream=["Ваниль", "Шоколад", "Клубничное", "Эскимо"]
#choise=str(input("Какой вкус хотите?"))
#if choise in ice_cream:
#    print("У нас есть такой вкус!")
#else:
#    print("Такого вкуса у нас нет")
#trees=["сосна", "берёза","осина"]
#print(trees)
#trees.append("Дуб")
#trees.append("Клён")
#trees.append("Сакура")
#trees.append("Баобаб")
#trees.append("Черёмуха")
#print("Новый список деревьев: ", trees)
class_4a=["Игорь", "Артём", "Маша"]
class_4b=["Максим", "Настя", "Матвей"]
print("Класс 4 а: ", class_4a)
print(" 4 б класс: ", class_4b)
class_4a.extend(class_4b)
print(class_4a)
#ice_creem = ["Пломбир", "48 копеек", "Золотой стандарт"]
#candy = ["Бон пари", "Мндмс", "Чупачупс"]
#snaks = ["Твикс", "Сникерс", "Марс"]
#print("Мороженое: ", ice_creem)
#print("Конфетки: ", candy)
#print("Шоколадки: ", snaks)
#candy.extend(snaks)
#candy.extend(ice_creem)
#print("Все сладости: ", candy)
print(sorted(class_4a))
numbers = [12, 4, 2, 56, 88, 1, 32, 27, -1]
print("Список чисел: \n", numbers)
print("Сортированный список: \n", sorted(numbers))
if -1 in numbers:
    print("У нас есть отрицательное число")
if "Наташа" in class_4a:
    print("Поздравляем, у Максима 1 место по плаванью")
