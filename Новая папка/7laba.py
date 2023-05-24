

from PIL import Image, ImageFilter
def ypr1():

 image = Image.open('1.png')
 width, height = image.size
 forma = image.format
 mode = image.mode
 image.show()

 print("ширина", width)
 print("высота", height)
 print("формат", forma)
 print("цветовая модель", mode)

ypr1()


def ypr2():
 image = Image.open('jinx.jpg')
 newimage = image.resize((image.width // 3, image.height // 3))
 newimage.save('rejinx.jpg')

 conimage = image.transpose(Image.FLIP_LEFT_RIGHT)
 conimage.save('flipjinx.jpg')
 conimage = image.transpose(Image.FLIP_TOP_BOTTOM)
 conimage.save('jinxflip.jpg')

ypr2()

def ypr3():
 images = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg']
 for file in images:
  image = Image.open(file)
  newimg = image.filter(ImageFilter.CONTOUR)
  newimg.show()
  newimg.save('new' + file)

ypr3()

def ypr4():

   with Image.open('watermark.jpg') as image:
    newimg = image.resize((image.width // 3, image.height // 3))
   with Image.open('meow.jpg') as image:
    image.paste(newimg)
   image.save('watermark1.jpg')


ypr4()


