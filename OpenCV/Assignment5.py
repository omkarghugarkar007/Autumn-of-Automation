import numpy as np
import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread('ball.jpg',0)          # queryImage

cap = cv2.VideoCapture('leomessi.mp4')
while(cap.isOpened()):
	ret, frame = cap.read()

	orb = cv2.ORB_create()


	kp1, des1 = orb.detectAndCompute(img1,None)
	kp2, des2 = orb.detectAndCompute(frame,None)

# create BFMatcher object
	bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=False)

# Match descriptors.
	matches = bf.match(des1,des2)

# Sort them in the order of their distance.
	matches = sorted(matches, key = lambda x:x.distance)

# Draw first 10 matches.
	img3 = cv2.drawMatches(img1,kp1,frame,kp2,matches[:10], flags=2)

	plt.imshow(img3),plt.show()

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
    
	cv2.waitKey(50)

cap.release()
cv2.destroyAllWindows()