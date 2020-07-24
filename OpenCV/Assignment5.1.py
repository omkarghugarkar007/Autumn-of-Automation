import numpy as np
import cv2

cap = cv2.VideoCapture('leomessi.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()

    blurred = cv2.GaussianBlur(frame, (11, 11), 0)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    greenLower = (29, 86, 6)
    greenUpper = (64, 255, 255)

    mask = cv2.inRange(gray, greenLower, greenUpper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    cnts = cv2.findContours(mask, 1, 2)[0]

    if len(cnts) > 0:

        for cnt in cnts:

            arc =0.01*cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, arc, True)

            if len(approx)>10:

                (x,y),radius = cv2.minEnclosingCircle(cnt)
                center = (int(x),int(y))
                radius = int(radius)
                area_e = 3.14*radius*radius
                area_c = cv2.contourArea(cnt)
                #print(area_c, end = " ")
                #print(area_e)

                if area_c > area_e - 2000 and area_c < area_e + 2000: 
                    if radius > 30 and radius < 70:
                        frame = cv2.circle(frame,center,radius,(0,255,0),2)

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    cv2.waitKey(50)

cap.release()
cv2.destroyAllWindows()
