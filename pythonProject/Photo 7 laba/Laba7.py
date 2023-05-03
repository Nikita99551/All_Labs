# 71 открывает картинку
# Показывает ее
# Получает ее высоту и ширину
# Выводит 4 характеристики картинки
#
# 72 открывает картинку
# Создаёт новое изображение уменьшив эту картинку в 3 раза
# Сохраняет ее
# Потом создаёт и сохраняет перевёрнутые картинки по горизонтали и по вертикали
#
# 73 объявили массив с именами файлов
# Для каждого файла: открыли файл, наложили серый фильтр, сохранили полученную картинку
from PIL import Image
filename ="photo (1).jpg"
with Image.open(filename) as img:
    img.load()
img.show()
format=img.format
mode=img.mode
width, height = img.size
print("Ширина= ",width)
print("Высота= ",height)
print("Формат= ",format)
print("Цветовая= ",mode)

def z2():
    filename = "photo (2).jpg"
    with Image.open(filename) as img:
        img.load()
        img.show()
    img = img.resize((img.width // 3, img.height // 3))
    img.save("pirock12.jpg")
    img1 = img.rotate(180)
    img1.save("rotate2.jpg")
    img1.show()
    img2 = img.transpose(Image.FLIP_LEFT_RIGHT)
    img2.save("img33.jpg")

def z3():
    filenames = ['photo (1).jpg', 'photo (2).jpg', 'photo (3).jpg', 'photo (4).jpg', 'photo (5).jpg']
    for filename in filenames:
        with Image.open(filename) as img:
            gray_img = img.convert("L")
            gray_img.save(f'gray_{filename}')

def z4():
    filename = "watermark.png"
    with Image.open(filename) as imw:
        imw.load()
    imw = imw.resize((imw.width // 4, imw.height // 4))
    photo2 = "photo (3).jpg"
    with Image.open(photo2) as img:
        img.load()
    img.paste(imw, (50, 50), imw)
    img.save("smile.jpg")
z2()
z3()
z4()