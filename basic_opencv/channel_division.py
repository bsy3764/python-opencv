import cv2

path = "/home/test/test/data/lena.jpg"
src = cv2.imread(path)

# 채널 별(b, g, r)로 이미지를 분리
b, g, r = cv2.split(src)
#imgRGB = cv2.merge((r, g, b))
imgBGR = cv2.merge((b, g, r))

cv2.imshow("b", b)
cv2.imshow("g", g)
cv2.imshow("r", r)
#cv2.imshow('imgRGB', imgRGB)
cv2.imshow('imgRGB', imgBGR)

cv2.waitKey()
cv2.destroyAllWindows()