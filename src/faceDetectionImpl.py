# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 19:58:18 2023

@author: sonan
"""

#import the required libraries
import sys

import face_recognition 
import cv2

print("All good")

#loading the image to detect
image_to_detect = cv2.imread("D:/face-emotion-recognition/image/people_emotion.jpg")

#detect all faces in the image
all_face_locations = face_recognition.face_locations(image_to_detect,model='hog')

#print the number of faces detected
print('There are {} no of faces in this image'.format(len(all_face_locations)))
print(sys.executable)

#looping through the face locations
for index,current_face_location in enumerate(all_face_locations):
 
    top_pos,right_pos,bottom_pos,left_pos = current_face_location
    #printing the location of current face
    print('Found face {} at top:{},right:{},bottom:{},left:{}'.format(index+1,top_pos,right_pos,bottom_pos,left_pos))
    current_face_image = image_to_detect[top_pos:bottom_pos,left_pos:right_pos]

    cv2.imshow("Face no "+str(index+1),current_face_image)
