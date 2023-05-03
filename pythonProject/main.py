N = int(input("Введите кол-во слов "))
a=""
for i in range(N):
    a=a + input()+" "
print(a)
def z2():
    a=[]
    b=str(input())
    while b!="stop":
        b=str(input())
        a.append(b)
    print(a)
z2()
def z3():
    a=0
    while a!="stop":
        a=input()
        if "ф" in a or "Ф" in a:
            print("Ого!Это редкое слово")
        else:
            print("Эх, это не очень редкое слово!")
z3()
def z4():
    from random import randint
    a1 = 0
    a2 = 0
    while a1 != 3:
        num1 = randint(1, 10)
        num2 = randint(1, 10)
        ans = int(input(f'{num1} + {num2} = '))
        if ans != (num1 + num2):
            a1 += 1
            print('Ответ неверный')
        else:
            a2 += 1
            print('Правильно!')
    print('Игра окончена. Правильных ответов:',)
z4()