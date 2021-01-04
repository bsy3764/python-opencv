from PIL import Image

path = "/home/test/test/data/lena.jpg"

im = Image.open(path)
img2 = im.rotate(90)
img2.show()