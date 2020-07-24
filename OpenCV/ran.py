import cv2
import numpy as np

img = cv2.imread("#", cv2.IMREAD_GRAYSCALE)
_, threshold = cv2.threshold(img, 240, 255, cv2.THRESH_BINARY)
contours,hierarchy= cv2.findContours(threshold, 1, 2)

font = cv2.FONT_HERSHEY_COMPLEX
cnt = contours[0]

arc =0.1*cv2.arcLength(cnt, True)
approx = cv2.approxPolyDP(cnt, arc, True)
cv2.drawContours(img, [approx], 0, (0), 5)

print(len(approx))
print(approx.shape)
print(approx)

if len(approx) == 3:
        print("Triangle")
elif len(approx) == 4:
        point_a = approx[0,:,:]
        point_b = approx[1,:,:]
        point_c = approx[2,:,:]
        dist1 = np.linalg.norm(point_a - point_b)
        dist2 = np.linalg.norm(point_b - point_c)

        epsilon = 6

        if dist1 > dist2 - epsilon and dist1 < dist2 + epsilon:

            slope1 = (point_a[:,1] - point_b[:,1])/(point_a[:,0] - point_b[:,0])
            slope2 = (point_b[:,1] - point_c[:,1])/(point_b[:,0] - point_c[:,0])
            epsilon = 0.1

            if  slope1*slope2 > -0.9 and slope1*slope2 < 1.1 :

                print("Square")

            else:

                print("Rhombus")
        else:
            print("Rectangle")

elif 6 < len(approx) < 15:
        print("Oval")
else:
        print("Circle")

cv2.imshow("Threshold", threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()