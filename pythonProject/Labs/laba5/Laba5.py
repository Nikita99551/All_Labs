import random
a=[1,2,3,4,5]
b=(int(input("Введите число: ")))
if b in a:
    print("Поздравляю,Вы угадали число!")
else:
    print("Нет такого числа!")

def z2():
    a=[1,4,4,4,5,7,9]
    for i in a:
        if a.count(i) > 1:
            print(i)

def z3():
    day=("Понедельник","Вторник","Среда","Четверг","Пятница","Суббота","Воскресенье")
    kol=int(input("Сколько выходных вы хотите? "))
    for i in day:
        print("Рабочие дни:",day[:-kol])
        print("Выходные:",day[-kol:])
        break

def z4():
    group1=["Кашкадамов","Лащев","Хавалиц","Давлетов"]
    group2=["Сергеев","Долмацын","Москвитина","Федорова"]
    mas=[]
    for i in range(2):
        a=random.choice(group1)
        mas.append(a)
        b=random.choice(group2)
        mas.append(b)
    mas=tuple(mas)
    mas=tuple(sorted(mas))
    print(*mas)
    if "Лащев" in mas:
        print("Лащев есть")
        print("Кол-во Лащева: ", mas.count("Лащев"))
    else:
        print("Лащева нет")

z2()
z3()
z4()