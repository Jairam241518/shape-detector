import cv2
# import numpy as np
# import PIL
# from matplotlib import pyplot as plt
# from PIL import Image, ImageDraw, ImageFont
# from numpy import asarray
# from webcolors import rgb_to_name


# utility function
def rgbToColor(pixelValueOfImage):
    if pixelValueOfImage[0] == 0 and pixelValueOfImage[1] == 0 and pixelValueOfImage[2] == 255:
        color = "Red"
    elif pixelValueOfImage[0] == 255 and pixelValueOfImage[1] == 0 and pixelValueOfImage[2] == 0:
        color = "Blue"
    elif pixelValueOfImage[0] == 0 and pixelValueOfImage[1] == 255 and pixelValueOfImage[2] == 0:
        color = "Green"
    else:
        color = "Orange"
    return color


img = cv2.imread("shapes.png")
# print(img)
# dataImage = asarray(img)
# px = img[648,398]
# print(px)
# print(dataImage[0, 0])
# print(img.shape)
# width = int(img.shape[1])
# height = int(img.shape[0])
# dim = (width, height)
# imageResize = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
# cv2.imshow("hey", img)
# cv2.waitKey(0)

# imgPIL = Image.fromarray(dataImage)
# imgPIL = Image.open("shapes.png")
# imageRGB = imgPIL.convert("RGB")


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, threshold = cv2.threshold(gray, 200, 200, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

i = 0
shapes = []

for contour in contours:
    if i == 0:
        i = 1
        continue
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)

    cv2.drawContours(img, [contour], 0, (0, 0, 255), 5)

    M = cv2.moments(contour)
    if M['m00'] != 0:
        x = int(M['m10'] / M['m00'])
        y = int(M['m01'] / M['m00'])
    else:
        x, y = 0, 0

    if len(approx) == 3:
        # pixelValue = imageRGB.getpixel((x, y))
        pixelValue = img[y, x]
        colorName = rgbToColor(pixelValue)
        # colorName = "red"
        # colorName = rgb_to_name(pixelValue, spec='css3')
        shapes.append([colorName.capitalize(), 'Triangle', (x, y)])
        cv2.putText(img, 'Triangle', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.3, 0, 1)

    elif len(approx) == 4:
        (x1, y1, w, h) = cv2.boundingRect(approx)
        if (float(w) / h) == 1:
            # pixelValue = imageRGB.getpixel((x, y))
            pixelValue = img[y, x]
            # colorName = "red"
            colorName = rgbToColor(pixelValue)
            # colorName = rgb_to_name(pixelValue, spec='css3')

            cv2.putText(img, "square", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, 0, 2)
            shapes.append([colorName.capitalize(), 'Square', (x, y)])
        else:
            # pixelValue = imageRGB.getpixel((x, y))
            pixelValue = img[y, x]
            # colorName = rgb_to_name(pixelValue, spec='css3')
            colorName = rgbToColor(pixelValue)
            # colorName = "red"
            # cv2.circle(img, (x, y), 7, (255, 255, 255), -1)

            cv2.putText(img, "rectangle", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, 0, 2)
            shapes.append([colorName.capitalize(), 'Rectangle', (x, y)])

        # cv2.putText(img, 'Quadrilateral', (x, y),
        # cv2.FONT_HERSHEY_SIMPLEX, 0.3, (255, 255, 255), 1)

    elif len(approx) == 5:
        # pixelValue = imageRGB.getpixel((x, y))
        pixelValue = img[y, x]
        colorName = rgbToColor(pixelValue)
        # colorName = rgb_to_name(pixelValue, spec='css3')
        shapes.append([colorName.capitalize(), 'Pentagon', (x, y)])
        cv2.putText(img, 'Pentagon', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.3, 0, 1)

    elif len(approx) == 6:
        # pixelValue = imageRGB.getpixel((x, y))
        pixelValue = img[y, x]
        # colorName = "red"
        colorName = rgbToColor(pixelValue)
        # colorName = rgb_to_name(pixelValue, spec='css3')
        shapes.append([colorName.capitalize(), 'Hexagon', (x, y)])
        cv2.putText(img, 'Hexagon', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.3, 0, 1)

    else:
        # pixelValue = imageRGB.getpixel((x, y))
        pixelValue = img[y, x]
        # colorName = "red"
        colorName = rgbToColor(pixelValue)
        # colorName = rgb_to_name(pixelValue, spec='css3')
        shapes.append([colorName.capitalize(), 'Circle', (x, y)])
        cv2.putText(img, 'circle', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, 0, 1)

# cv2.imshow('shapes', img)
print(shapes)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

