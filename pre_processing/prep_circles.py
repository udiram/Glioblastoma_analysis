import cv2
import numpy as np

image = cv2.imread('../data/uab_data/keras/recurrent/CoreID3.jpg')
# crop_img = image[0:250, 50:400]
crop_img = cv2.medianBlur(image, 25)
original = crop_img.copy()

gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
# thresh_inv = cv2.bitwise_not(thresh)
ROI_number = 0
cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
# for c in cnts:
sort_cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
x,y,w,h = cv2.boundingRect(sort_cnts[0])
cv2.rectangle(crop_img, (x, y), (x + w, y + h), (0,0,255), 2)


x_crop = x + 50
y_crop = y + 50
w_crop = w - 100
h_crop = h - 100

cv2.rectangle(crop_img, (x_crop, y_crop), (x_crop + w_crop, y_crop + h_crop), (0,255,0), 2)

new_img = image[y_crop:y_crop + h_crop, x_crop:x_crop + w_crop]
cv2.imshow('new_img', new_img)
cv2.imshow('image', crop_img)
cv2.imshow('Thresh',thresh)
cv2.waitKey()