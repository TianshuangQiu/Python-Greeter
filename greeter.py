import cv2
import os
import pygame
from gtts import gTTS
import importlib


def create_file(word):
    """
    Generates the greeter audio file for an object

    word:      must be a string
    returns:    the location of the saved file as a string
    """
    text = "Hello " + word
    sound = gTTS(text=text, lang="en", slow=False)
    text = text.replace(" ", "_")
    file_name = f"Saved/{text}.mp3"
    sound.save(file_name)


def play_file(path):
    """
    Plays the audio of a file

    path: path to the file
    """
    pygame.mixer.init()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play(0)
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


# capture and save an image
vid = cv2.VideoCapture(0)
ret, frame = vid.read()
img_name = "captured.png"
cv2.imwrite(img_name, frame)
vid.release()

moduleName = input("watson.py")
importlib.import_module(moduleName)
model = make_yolov3_model()
weight_reader = WeightReader('yolov3.weights')
weight_reader.load_weights(model)
model.save('model.h5')
