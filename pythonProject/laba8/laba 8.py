# 8.1) Скачайте любую открытку из интернета, определите область, которую Вам нужно вырезать из
# данного изображения (обрезать текст, часть фото и т.д.). Напишите программу, которая выполнит эту
# операцию. Сохраните изображения в текущую папку под новым именем.
#
# 8.2) Создайте словарь, содержащий перечень пары «Название праздника – имя_файла с открыткой к нему».
# Спросите у пользователя, к какому празднику ему нужна открытка и выведите нужную открытку на экран.
#
# 8.3) Модифицируйте задачу 8.1 так: спросите еще у пользователя, имя того, кого он хочет поздравить,
# добавьте на заданную открытку текст «…., поздравляю!», где вместо …. вставьте полученное имя
# (выведите его разным цветом и шрифтами, посередине вверху или внизу фото). Найдите в сети интернет
# решение, как сделать надпись жирным текстом (по умолчанию, такого параметра нет). Сохраните новую открытку в файл с расширением png.

from PIL import Image, ImageFont, ImageDraw
img=Image.open("da.jpg")
area=(100,150,300,300)
img.load()
img.show()
cut=img.crop(area)
cut.show()
img.save("bobik.jpg")

def z2():
    import os
    from PIL import Image
    prazdnik={
        "Новый год":"new__year.jpg",
        "8 Марта":"8 marta.jpg",
        "23 Февраля":"23fev.jpg",
        "День рождения":"happy__birthday.jpg"
    }
    budet=input("Введите название праздника: ")
    if budet in prazdnik:
        prazdnik__budet=prazdnik[budet]
        prazdnik__os=os.path.abspath(prazdnik__budet)
        print("Открытка для праздника",{budet},":")
        print(prazdnik__os)
        image = Image.open(f"{prazdnik__os}")
        image.show()
    else:
        print("Такого праздника нету в списке ")

def z3():
    spisok = {'Новый год': 'new__year.jpg', '23 Февраля': '23fev.jpg', 'День рождения': 'happy__birthday.jpg', '8 Марта': '8 marta.jpg'}
    budet = input('Какой праздник? ')
    name = input('Какое имя? ')
    for i in spisok:
        if budet == i:
            im = Image.open(spisok[i])
            font = ImageFont.truetype('RubikWetPaint-Regular.ttf', size=im.width // 20)
            img = ImageDraw.Draw(im)
            img.text(
                (im.width // 5, 10),
                name + ', поздравляю',
                font=font,
                fill='#FF0000',
                stroke_width=2,
                stroke_fill="#FF0000")
            im.save(i + '.png')
        break
    else:
        print('Нет такой открытки(')
z2()
z3()
