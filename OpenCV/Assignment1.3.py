import cv2
import matplotlib.pyplot as plt

bgr_img = cv2.imread("sachin.jpg",1)

rgb_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2RGB)

cv2.imwrite("red_to_blue.png", rgb_img)

cv2.imshow("Red_to_BLue",rgb_img)

cv2.waitKey(0)

cv2.destroyAllWindows()

quit()
