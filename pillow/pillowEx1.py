from PIL import Image

path = "/home/test/test/data/lena.jpg"

im = Image.open(path)
size = (64, 64)
im.thumbnail(size)  # 썸네일 만들기
print(im.size)  # 이미지 크기 출력
im.show()

outpath = "/home/test/test/data/pillow_lena.jpg"
im.save(outpath)

outpath1 = "/home/test/test/data/thumbnail_lena.jpg"
im.save(outpath1)
