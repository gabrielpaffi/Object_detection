import detect1
import cv2

image = 0
weights = "Cube.pt"
conf_thres = 0.4


b = detect1.detecti(image,weights,conf_thres)
print(b)
