list_of_products = {"Фрукты":["Яблоки", "Бананы", "Мандарины"],
                    "Овощи":["Картофель", "Морковь", "Лук", "Помидор"],
                    "Кисломолочные":["Молоко", "Яйца", "Сыр"],
                    "Мясо":["Куринное филе", "Свинина"]}
list_for_home = {"Товары для ремонта":["Обои", "Клей для обоев", "Лампочки"],
                 "Мебель":["Стол", "Стулья", "Диван"],
                 "Украшения":["Люстра", "Занавески"]}
def spisochek(chto_to):
    for i in chto_to:
         print(i)    
    print("Выберете Категорию")
    choice = input()
    for prod in chto_to[choice]:
        print(prod)

#spisochek(list_for_home)
#spisochek(list_of_products)
def first_func():
    a = 9**2
    return a
b = first_func()*6
print(b)
def second_func(cifra):
    return cifra ** 2
print(second_func(11))
def hello(imya):
    return "Привет," + imya

print(hello("Максим"))










