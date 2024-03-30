
import numpy as np
import cv2 
import detect1


import random
import time

from argon2 import PasswordHasher

import speech_recognition as sr
import speech


def yolod():


	
	phrase = speech.speech()
	print("j'ai entendu :",phrase)


	objects = ["mug","balle", "Cube", "moi"]

	objectr = "3objets"
	conf_thres = 0.2


	for i in range(len(objects)):
		
		if (phrase.find(objects[i]) >= 0 ):
			objectr = objects[i]
			conf_thres = 0.5

			break


	weights = objectr+".pt"
	print(weights)
	
	


	def photo():
		cap = cv2.VideoCapture(0)
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
			cv2.imshow("logitech",frame)
			if cv2.waitKey(1) == ord('q'):
				image = "image.jpg"
				cv2.imwrite(image,frame)
				break
				
		# When everything done, release the capture
		cap.release()
		cv2.destroyAllWindows()
		return image

	image = photo()
	print(image)

	'''

	img=cv2.imread (image)
	cv2.imshow('image',img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	'''



	coordonnees_camera = detect1.detecti(image,weights,conf_thres)
	print(type(coordonnees_camera) )
	
	return coordonnees_camera
