from PIL import Image

path = "/home/test/test/data/lena.jpg"

im = Image.open(path)
img2 = im.crop((100, 100, 350, 350))    # 튜플로 크기가 들어가야 함
img2.show()
