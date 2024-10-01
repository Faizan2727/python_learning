# Loops in python are used to perform repetitive tasks efficiently. Here are some keys reasons why we use loops:
# Automation of repetative Tasks.
# Iterating Over Data Structures.
# Conditional repetation.
# Processing Items in Bulk.

# A for loop in python is used to iterate over a sequence (such as a list, tuple, dictionary, set amd strings) and excute a block of code for each item in the sequence.

words = ["first", "second", "third", "Fourth"]
for x in words:
    print(x)


# A while loop i python repeatedly excutes a block of codes as long as a given condition is true.

# An infinite while loop in Python runs indefinitely unless interrupted by a break statement or an external action like a keyboard interrupt ( ctrl+C )

# Infinite loops are useful in scenerios where you need a program to keep running a until a certain condition is met, such as continously checking for user input or monitoring a system status.

#page = 1
#while page <= 10:
#    print("eassy")
#else:
#   print("no")


# Video Processing 

# A video is sequence of still images called frames, displayed quickly one after another. The speed at which these frames are show is called the frame rate measured in frames oer second (fps). Common frame rates include 24 fps , 30 fps and 60 fps.

# We can capture a video from your camera by using an infinite while loop in python.
import cv2

cap = cv2.VideoCapture(0)
while True:
    status, photo = cap.read()
    cv2.imshow("Faizan Photo", photo)
    if cv2.waitKey(100) == 13: #if you want to close window then you have to use waitKey function and that 13 is for enter when we press enter it wll close the window.
        break

cv2.destroyAllWindows()

# cv2.imshow("Faizan Photo", photo[100:200, 200:400]) by this u can crop the video by using numpy array

# You can perform any action on a video that you can do on an image.
# You can stream your mobile phones camera video to python by using the ip webcam mobile application.
# The application will give you a web link that you have to copy in your python code.

# eg
# cap = cv2.VideoCapture("https://192.168.0.103:8080/video") 
# By this you can create your own cctv camera :)


