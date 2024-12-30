import cv2
image = cv2.imread("example2.jpg")
image_grey = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
image_invert = 255 - image_grey

blurred = cv2.GaussianBlur(image_invert , (21,21) , 0)
inverted_blur = 255 - blurred
pencil = cv2.divide(image_grey , inverted_blur , scale=256.0)

cv2.namedWindow("Original" , cv2.WINDOW_NORMAL)
cv2.namedWindow("Sketch" , cv2.WINDOW_NORMAL)

cv2.imshow("Original" , image)
cv2.imshow("Sketch" , pencil)
cv2.waitKey(0)
