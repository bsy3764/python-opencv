import cv2

path = "/home/test/test/data/lena.jpg"

src = cv2.imread(path)
# 흐릿하게 문대기
# (4, 4)크기만큼 <-- 해당 숫자가 클 수록 더 흐릿하게 됨
dst1 = cv2.blur(src, (4, 4), anchor=(-1, -1), borderType=cv2.BORDER_DEFAULT)
dst2 = cv2.blur(src, (9, 9), anchor=(-1, -1), borderType=cv2.BORDER_DEFAULT)

cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst2)

cv2.waitKey(0)
cv2.destroyAllWindows()