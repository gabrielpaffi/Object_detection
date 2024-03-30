
import numpy as np
import cv2 as cv


def photo():
	cap = cv.VideoCapture(2)
	if not cap.isOpened():
		print("Cannot open camera")
		exit()
	while True:
		# Capture frame-by-frame
		ret, frame = cap.read()
		# if frame is read correctly ret is True
		if not ret:
			print("Can't receive frame (stream end?). Exiting ...")
			break
		# Our operations on the frame come here
		b = frame
		# Display the resulting frame
		cv.imshow("logitech",frame)
		if cv.waitKey(1) == ord('q'):
			image = "image.jpg"
			cv.imwrite(image,frame)
			break
			
	# When everything done, release the capture
	cap.release()
	cv.destroyAllWindows()
	return image

image = photo()
print(image)
