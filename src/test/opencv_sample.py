import cv2

img1 = cv2.imread("125.jpg", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("124.jpg", cv2.IMREAD_GRAYSCALE)
img3 = cv2.imread("125.jpg", cv2.IMREAD_GRAYSCALE)

element = cv2.getStructuringElement(cv2.MORPH_RECT, (13, 5))

# out1 = cv2.erode(img2, element)

blur = cv2.GaussianBlur(img1, (5, 5), 0)

# con1 = cv2.threshold(img1,50,255,cv2.THRESH_BINARY_INV)
# print con1

close = cv2.morphologyEx(blur, cv2.MORPH_CLOSE, element)
open = cv2.morphologyEx(close, cv2.MORPH_OPEN, element)

con = cv2.morphologyEx(open, cv2.MORPH_TOPHAT, element)

_, binary = cv2.threshold(open, 120, 255, cv2.THRESH_BINARY_INV)

# _, contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

res = cv2.Canny(binary, 10, 255)


cv2.imshow("shit", res)
cv2.imshow("fuck", img1)




cv2.waitKey(0)

print ("fuck")
