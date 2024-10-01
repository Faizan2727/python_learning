# If we want to detect fingers we can use cvzone library. Install the library using pip. This library also depends on tzdata library.

# pip install cvzone

# Now click the photo use the following code-

#import cv2
#cap = cv2.VideoCapture(0)
#status, photo = cap.read()
#cv2.imshow('Faizan', photo)
#cv2.waitKey()
#cv2.destroyAllWindows()

# Now to detct the finger use the following code-
# from cvzone.HandTrackingModule import HandDetector

# Import the HandDetector class from the HandTrackingModule in the cvzone library. The Cvzone library is used for computer vision tasks, and the HandTrackinModule is specially for detecting and tacking hands

# detector = HandDectector()

# Creates an instance of the HandDetector class which is used to perform hand detection.
# detector.findHands(photo)

# Uses The findHands method of the HandDetector instance to detect hands in the provided photo variable the photo is likely an image in which the hand detection is being performed.

# Now id we see the photo it gives 21 landmarks-

# It has co-ordinates of every finger.
# If we have co-ordinates we can find the distance between two fingers.


# Now store the value of fingers in a variable. And now detect it will give you array like this-
# HandlmList = findhand[0][0]
# detector.fingersUp(HandlmList)
# [1,0,0,0,0]

# HandlmList = findHand[0][0]
# findHand[0] refers to first hand detected.
# [0] after findHand[0] is accessing the landmark list for this hand.

# detector.fingersUp(HandlmList)
# Calls the fingersUp method of the HandDectector instance, passing in the HandlmList. The FingersUp method process the landmark list to determine which finger are up.

# [1,0,0,0,0]
# 1 indicates that the thumb is up.
# 0 indicates that the index finger is not up.
# The remaining 0s indicates that the middle finger, ring finger and little finger are not up.
# Now we can use this launch different programs using finger gesture using the following code-


# status, photo = cap.read()
# findHand = detector.findHands(photo1)

# HandlmList = findHand[0][0]
# fingerUpDetect = detctor.fingersUp(HandlmList)

# if fingerUpDetect == [0,1,1,0,0]:
#   os.system("chrome")
# elif fingerUpDetect == [0,1,0,0,0]:
#   os.system("notepad")
# elif  fingerUpDetect == [1,1,1,1,1]:
#   os.system("paint")
#else:
#   print("idk")

# fingerUpDetect is a list that indicates which fingers are up.  

#The if statement checks if fingerUpDetect is [0, 1, 1, 0, 0] (index and middle fingers up, others down). If true, it runs the system command chrome to open the Chrome browser.  

#The first elif statement checks if fingerUpDetect is [0, 1, 0, 0, 0] (only the index finger up). If true, it runs the system command notepad to open Notepad.  

#The second elif statement checks if fingerUpDetect is [1, 1, 1, 1, 1] (all fingers up). If true, it runs the system command paint to open Microsoft Paint.  

#The else statement handles any other case, printing "idk" (short for "I don't know").

#If we want it to be in video we can put it in while loop . Also we can add condition to to check if the hand exists or not so that code does not fail .

import cv2
import os
from cvzone.HandTrackingModule import HandDetector
detector = HandDetector()

cap = cv2.VideoCapture(0)
while True:
    status, photo = cap.read()
    findHand = detector.findHands(photo)
    
    if findHand[0]:
        HandlmList = findHand[0][0]
        fingerUpDetect = detector.fingersUp(HandlmList)

        if fingerUpDetect == [0,1,1,0,0]:
            os.system("chrome")
        elif fingerUpDetect == [0,1,0,0,0]:
            os.system("notepad")
        elif  fingerUpDetect == [1,1,1,1,1]:
            os.system("paint")
        else:
            print("idk")


# cvzone has its github repository, Here lots of other detecting models are available.

# https://github.com/cvzone/cvzone





