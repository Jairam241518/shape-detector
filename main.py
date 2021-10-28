import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("shapes.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, threshold = cv2.threshold(gray, 200, 200, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

i = 0
shapes = []

for contour in contours:
    if i==0:
        i=1
        continue
    approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)

    cv2.drawContours(img, [contour], 0, (0,0,255), 5)

    M = cv2.moments(contour)
    if M['m00'] != 0.0:
        x = int(M['m10']/M['m00'])
        y = int(M['m01'] / M['m00'])

    if len(approx) == 3:
        shapes.append(['Triangle', (x,y)])
        cv2.putText(img, 'Triangle', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.3, 0, 1)

    elif len(approx) == 4:
        (x, y, w, h) = cv2.boundingRect(approx)
        if ((float(w)/h) == 1):
            cv2.putText(img, "square", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, 0, 2)
            shapes.append(['Square', (x, y)])
        else:
            cv2.putText(img, "rectangle", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, 0, 2)
            shapes.append(['Rectangle', (x, y)])

        #cv2.putText(img, 'Quadrilateral', (x, y),
                    #cv2.FONT_HERSHEY_SIMPLEX, 0.3, (255, 255, 255), 1)

    elif len(approx) == 5:
        shapes.append(['Pentagon', (x, y)])
        cv2.putText(img, 'Pentagon', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.3, 0, 1)

    elif len(approx) == 6:
        shapes.append(['Hexagon', (x, y)])
        cv2.putText(img, 'Hexagon', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.3, 0, 1)

    else:
        shapes.append(['Circle', (x, y)])
        cv2.putText(img, 'circle', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, 0, 1)

cv2.imshow('shapes', img)
print(shapes)

cv2.waitKey(0)
cv2.destroyAllWindows()
