countries_dict = {"Австрия": "Вена", "Бельгия": "Брюссель", "Великобритания": "Лондон", "Германия": "Берлин",
                  "Ирландия": "Дублин", "Лихтенштейн": "Вадуц", "Нидерладны": "Амстердам",
                  "Франция": "Париж", "Белоруссия": "Минск", "Болгария": "София", "Польша": "Варшава", "Чехия": "Прага",
                  "Албания": "Тирана", "Босния и Герцеговина": "Сараево",
                  "Северная Македония": "Скопье", "Сербия": "Белград"}

print(countries_dict)
print(countries_dict["Австрия"])
for i in sorted(countries_dict):
    print(i, " - ", countries_dict[i])


def z2():
    alph = {
        "а": 1,
        "б": 3,
        "в": 1,
        "г": 3,
        "д": 2,
        "е": 1,
        "ё": 3,
        "ж": 5,
        "з": 5,
        "и": 1,
        "й": 4,
        "к": 2,
        "л": 2,
        "м": 2,
        "н": 1,
        "о": 1,
        "п": 2,
        "р": 1,
        "с": 1,
        "т": 1,
        "у": 2,
        "ф": 10,
        "х": 5,
        "ц": 5,
        "ч": 5,
        "ш": 8,
        "щ": 10,
        "ъ": 10,
        "ы": 4,
        "ь": 3,
        "э": 8,
        "ю": 8,
        "я": 3
    }
    slovo = input("Введите слово: ")
    s = 0
    for i in slovo:
        s += alph[(i.lower())]
    print("Сумма: ", s)






#    student = {"Петров", "Беглов", "Иванов", "Щеглов", "Бобров"}
#    language = {"Английский", "Русский", "Немецкий", "Французский", "Турецкий"}
 #   language2 = {"Китайский"}
  #  print(sorted(language))

students = {
    "John": {"English", "Spanish", "Chinese"},
    "Emily": {"French", "Chinese"},
    "Sara": {"English", "German", "Chinese", "Russian"},
    "David": {"English", "Chinese", "Japanese"},
    "Anna": {"Chinese", "Korean"}
}

# Список всех языков, которые знают студенты
all_languages = set()
for languages in students.values():
    all_languages.update(languages)
sorted_languages = sorted(all_languages)

# Список студентов, которые знают китайский язык
chinese_speakers = []
for student, languages in students.items():
    if "Chinese" in languages:
        chinese_speakers.append(student)

print("Список всех языков, которые знают студенты:", sorted_languages)
print("Список студентов, которые знают китайский язык:", chinese_speakers)
z2()
