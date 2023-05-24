from PIL import Image, ImageFont, ImageDraw

def ypr1():

    image = Image.open('postcard.jpg')
    imcrop = image.crop((100, 100, 400, 400))
    imcrop.save('imcropped.jpg')
    imcrop.show()



def ypr2():
    s = {'Новый год': 'newyear.jpg', '8 марта': '8march.jpg', '1 мая': '1may.jpg', 'День Святого Валентина': 'love.jpg'}
    p = input('Какой праздник? ')
    img = Image.open(s[p])
    img.show()



def ypr3():

    image = Image.open('postcard.jpg')
    name = input('Введите имя: ')
    fon = ImageFont.truetype('Nevduplenysh-Regular.otf', 40)
    img = ImageDraw.Draw(image)
    img.text((40, 400), name + ', поздравляю!', font = fon, fill = 'white')
    image.show()

ypr3()

