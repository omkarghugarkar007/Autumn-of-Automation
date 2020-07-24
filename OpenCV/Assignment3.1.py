import cv2

img = cv2.imread("sachin.jpg", 0)

edges = cv2.Canny(img,100,200)

cv2.imshow("Sketch", edges)

cv2.waitKey(0)

cv2.destroyAllWindows()

quit()