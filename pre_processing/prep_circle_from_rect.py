import cv2
import numpy as np

image = cv2.imread('../data/uab_data/keras/primary/1_N.jpg')

copy = image.copy()


dimensions = image.shape

# height, width, number of channels in image
height = image.shape[0]
width = image.shape[1]
channels = image.shape[2]

# draw filled circles in white on black background as masks
mask1 = np.zeros_like(image)
mask1 = cv2.circle(mask1, (int(width/2), int(height/2)), int(height/2), (255,255,255), -1)
dst = cv2.bitwise_and(mask1, image)

print('Image Dimension    : ', dimensions)
print('Image Height       : ', height)
print('Image Width        : ', width)
print('Number of Channels : ', channels)

# get (i, j) positions of all RGB pixels that are black (i.e. [0, 0, 0])
black_pixels = np.where(
    (dst[:, :, 0] == 0) &
    (dst[:, :, 1] == 0) &
    (dst[:, :, 2] == 0)
)

# set those pixels to white
dst[black_pixels] = [255, 255, 255]

cv2.circle(image, (int(width/2), int(height/2)), int(height/2), (0,0,255), 2)
cv2.rectangle(image,(0,0), (width, height), (0,255,0), 5)
cv2.imshow('image', image)
cv2.imshow('mask', mask1)
cv2.imshow('dst', dst)
cv2.waitKey()