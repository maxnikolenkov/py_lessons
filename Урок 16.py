"""
user_list = ["Никита", "Аня", "Миша"]
for i in user_list:
    print(i)

user_dict = {"name":["Антон", "Максим", "Нина"], "age":[14, 15, 16]}
print(user_dict)

for i in range(3):
    print(user_dict["name"][i], end="-")
    print(user_dict["age"][i])
"""
    
print("Здравствуйте, вы пришли в наш ресторан. Ознакомьтесь с меню")
meal = [
    {"name":"Стейк","cost":1750},
    {"name":"Гарнир из картофеля", "cost": 325},
    {"name":"Борщ", "cost":780},
    {"name":"Клубничный лимонад", "cost": 425},
    {"name":"Хлеб", "cost": 50}
    ]
for i in meal:
    print(i["name"],"-", i["cost"])

fruits = ["Яблоки","Апельсины","Бананы","Мандарины"]
fruits_dict = dict(enumerate(fruits))
print(fruits_dict)

a = ["Имя", "Возраст", "Город"]
b = ["Иван", 15, "Москва"]
c = ["Максим", 22, "Новосибирск"]
d = ["Артём", 21, "Благовещенск"]
person = dict(zip(a,c))
print(person)
    
