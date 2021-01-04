from PIL import Image, ImageFilter
import os
path = "/home/test/test/data/lena.jpg"

if os.path.isfile(path):
    im = Image.open(path)
    print("정상으로 읽음")
else:
    print("파일이 존재하지 않습니다.")

img2 = im.filter(ImageFilter.BLUR)
img2.show()