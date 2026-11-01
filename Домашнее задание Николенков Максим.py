print("ЗАДАНИЕ 1")
ratings_list = [5, 4, 5, 3, 4, 5, 5, 3, 4, 2]
ratings_set = set(ratings_list)
print("1. Вывод множества", ratings_set)
print("2. Вывод списка:", ratings_list)
print("3. Всего оценок:", len(ratings_list))
print("4. Количество разных оценок:", len(ratings_set))
    
print("ЗАДАНИЕ 2")
a_list = ["яблоко", "банан", "груша", "яблоко"]
b_list = ["банан", "киви", "груша", "апельсин"]
a_set = set(a_list)
b_set = set(b_list)
print(f"Любимые фрукты Ани:{a_set}\nЛюбимые фрукты Бориса:{b_set}")
both_favorite = a_set & b_set
print("Оба любят:", both_favorite)
one_favorite = a_set | b_set
print("Любит хотя бы один:", one_favorite)

print("ЗАДАНИЕ 3")
#Списки и множества возьмем из задания 2
a_favorite = a_set - b_set
b_favorite = b_set - a_set
print("Любит только Аня:", a_favorite)
print("Любит тлько Борис:", b_favorite)

print("ЗАДАНИЕ 4")
children = {"Аня", "Борис", "Вика", "Гоша"}
check_children = {"Аня", "Дима", "Вика"}
print("--Проверка--")
for _ in check_children:
    print(_, "есть?", _ in children)
children.add("Дима")
print("Добавили Дима")
print("Дима теперь есть?", "Дима" in children)
print("Все ученики:", children)
print("Количество учеников", len(children))
       


