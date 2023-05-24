from PIL import Image
def ypr1():
    im = Image.open('сдр.jpeg')
    im_crop = im.crop((10, 10, 300, 400))
    im_crop.save('сдр.jpeg')
    im_crop.show()

ypr1()

def ypr2():
   
    spisok = {
        "Новый год": "ng.jpeg",
        "День рождения": "сдр.jpeg",
        "День святого Валентина": "val.jpeg",
        "День матери": "8-marta15.jpeg"
    }

    name_day = input("К какому празднику вам нужна открытка - ").lower()
    for key, value in spisok.items():
        if name_day not in key:
            print("Этого праздника в словаре нет")
            break
        else:
            print("Хороший выбор! Открытка - {:.0f}".format(180))
            print(value)


ypr2()

def ypr3():
    from PIL import Image, ImageDraw, ImageFont

    name = input("Введите имя получателя: ")
    filename = "pasha.jpeg"
    with Image.open(filename) as img:
        img.load()
    font = ImageFont.truetype("arial,ttf", 30)
    draw_text = ImageDraw.Draw(img)
    draw_text.text(
        (img.width // 2 - 100, 15),
        name + ", поздравляю!",
        font = font,
        fill=('red')
    )
    img.show()
    img.save(name + "pasha.jpeg")

ypr3()