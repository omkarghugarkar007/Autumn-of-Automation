import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread("sachin.jpg",0)

img2 = cv2.imread("sachin.jpg")
gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

cv2.imshow("Black and White",img1)

cv2.imshow("Gray_Scale",gray)

cv2.waitKey(0)

cv2.destroyAllWindows()

quit()