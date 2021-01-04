import cv2
import os
import numpy as np

path = "/home/test/test/data/lena.jpg"
# 동영상 파일이 있으면 읽어옴

if os.path.isfile(path):
    src = cv2.imread(path)
else:
    print("파일이 존재하지 않습니다.")

b, g, r = cv2.split(src)

height, width, channel = src.shape
print(height, width, channel)

height, width = b.shape
print(height, width)

# 흰 색으로 만들기(0로 채워진 배열을 만들기)
zero = np.zeros((height, width, 1), dtype=np.uint8)
print(type(zero))
print(zero.shape)

imgB = cv2.merge((b, zero, zero))   # bgr의 gr을 0으로 채운 배열로 변경, 블루만 보이게 함
imgG = cv2.merge((zero, g, zero))
imgR = cv2.merge((zero, zero, r))

cv2.imshow('imgB', imgB)
cv2.imshow('imgG', imgG)
cv2.imshow('imgR', imgR)

cv2.waitKey(0)
cv2.destroyAllWindows()