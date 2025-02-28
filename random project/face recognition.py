#importing the required libraries
import cv2 
import numpy as np
#import face_recognition    #library required to download 
import csv
from datetime import datetime

#creating a variable to capture the video or the face
vedio_capture=cv2.VideoCapture(0)

#load faces from the pc or some database

