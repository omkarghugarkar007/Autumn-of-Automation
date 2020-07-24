import cv2

vid = cv2.VideoCapture(0)

while(True):

	ret,frame = vid.read()

	edges = cv2.Canny(frame,100,200)

	cv2.imshow('Frame', edges)

	if cv2.waitKey(1)  & 0xFF == ord('q'):
		break

vid.release()

cv2.destroyAllWindows()