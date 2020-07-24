import cv2
import numpy as np

img = cv2.imread('T.png',1)
rows,cols = img.shape[0],img.shape[1]

M = np.float32([[1,0,30],[0,1,0]])
dst1 = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('img1',dst1)

M = np.float32([[1,0,-30],[0,1,0]])
dst2 = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('img2',dst2)

M = np.float32([[1,0,0],[0,1,30]])
dst3 = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('img3',dst3)

M = np.float32([[1,0,0],[0,1,-30]])
dst4 = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('img4',dst4)

M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
dst5 = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('img5',dst5)

M = cv2.getRotationMatrix2D((cols/2,rows/2),180,1)
dst6 = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('img6',dst6)

M = cv2.getRotationMatrix2D((cols/2,rows/2),270,1)
dst7 = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('img7',dst7)

M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
dst7 = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('img7',dst7)

pts1 = np.float32([[30,30],[110,30],[30,110],[110,110]])
pts2 = np.float32([[0,0],[100,0],[0,100],[100,100]])
M = cv2.getPerspectiveTransform(pts1,pts2)
dst8 = cv2.warpPerspective(img,M,(100,100))
cv2.imshow('img8', dst8)

bilateral = cv2.bilateralFilter(img, 15, 75, 75)
cv2.imshow('img9', bilateral) 

gaussianblur = cv2.GaussianBlur(img, (5, 5), 0)
cv2.imshow('img10',gaussianblur)

cv2.waitKey(0)

cv2.destroyAllWindows()

quit()