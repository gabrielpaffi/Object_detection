import random
import time
from argon2 import PasswordHasher

import speech_recognition as sr
import speech

phrase = speech.speech()
print("j'ai entendu :",phrase)


objects = ["tasse", "bouteille", "balle de tennis", "Rubik's Cube", "pomme",]

objectr = "0"

for i in range(len(objects)):
    
    if (phrase.find(objects[i]) >= 0 ):
        objectr = objects[i]
        break


fichierpt = objectr+".pt"
print(fichierpt)