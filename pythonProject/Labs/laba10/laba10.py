# 10.1) #Имеется файл JSON с информацией о продуктах:
# products:
#   {
#        "name": "Шоколад",
#        "price": 50,
#        "available": true
#       "weight": 100
#   },
#   {
#       "name": "Кофе",
#       "price": 100,
#       "available": false,
#       "weight": 250
#   },
#   {
#       "name": "Чай",
#       "price": 70,
#       "available": true,
#       "weight": 50
# }
# Напишите программу, которая считывает информацию из этого файла и выводит ее на экран в виде:
# Название: Шоколад
# Цена: 50
# Вес: 100
# В наличии

# Название: Кофе
# Цена: 100
# Вес: 250
# Нет в наличии!

# Название: Чай
# Цена: 70
# Вес: 50
# наличии
# 10.2) Модифицируйте программу 10.1 – добавьте в нее код, который добавляет данные в файл JSON(спрашивает их у пользователя) и потом также выводить содержимое итогового файла на экран.
# 10.3) Создание русско - английского словаря. Имеется файл en - ru.txt, в котором находятся строки англо - русского словаря в таком формате:
# cat - кошка
# dog - собака
# home - домашняя
# папка, дом
# mouse - мышь, манипулятор мышь
# to do - делать, изготавливать
# to make – изготавливать
# Требуется создать русско-английский словарь и вывести его в файл ru-en.txt в таком формате:
# делать – to do
# дом – home
# домашняя папка – home
# изготавливать – to do, to make
# кошка – cat
# манипулятор мышь – mouse
# мышь – mouse
# собака – dog

import json
def z1():
    with open("products.json", "r") as file:
        data = json.load(file)
    new_product = {
        "name": input("Введите название продукта: "),
        "price": int(input("Введите цену продукта: ")),
        "available": input("Есть ли продукт в наличии (да/нет)? ") == "да",
        "weight": int(input("Введите вес продукта: "))
    }
    data["products"].append(new_product)
    with open("products.json", "w") as file: #запись
        json.dump(data, file, indent=2)
    print("Содержимое файла:")
    for product in data["products"]:
        print("Название:", product["name"])
        print("Цена:", product["price"])
        print("Вес:", product["weight"])
        if product["available"]:
            print("В наличии")
        else:
            print("Нет в наличии!")
        print()
z1()


def z2():
    with open("en-ru.txt", "r") as file:
        lines = file.readlines()
    dictionary = {}
    for line in lines:
        words = line.strip().split(" - ")
        english = words[0]
        russian = words[1].split(", ")
        for word in russian:
            if word not in dictionary:
                dictionary[word] = [english]
            else:
                dictionary[word].append(english)

    with open("ru-en.txt", "w") as file:
        for russian, english in sorted(dictionary.items()):
            file.write(f"{russian} - {', '.join(english)}\n")
z2()
