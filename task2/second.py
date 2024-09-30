# You cant do anything without function in computer system.
# Every module that comes with python is know as Built-in modules.
# The functions that comes with python you have to import those modules.
# If you want to use a camera using python you have to import the cv2 module.

import cv2

# In cv2 there is a function called VideoCapture to open your camera.
# Cap.read will read the camera and give 2 output "status" and "photo".
# The cv2.imshow() will show you the photo clicked by the camera.

cap = cv2.VideoCapture(0)
status, photo = cap.read()
cv2.imshow("Faizan Photo", photo)

# When you open a window, you have to tell the system how much time you have to open it.
# Wait Key fucntion will open the window for a particular time.
# In cv2 there is destroyAllWindows fucntion which will destroy the window.

cv2.waitKey()
cv2.destroyAllWindows()

# A digital images is nothing it is only a 3D numpy array with RGB colors.
print(type(photo))

# In digital images the color of each pixel isnt't stored directly but rather represented by numerical value that correspond to color codes, typically in the RGB(Red , Green, Blue) color model. Each pixel color is defined by three values, one of each for red, green and blue components, which when combined create the final color seen on the screen.

# If you want to check the shape of the image then use photo.shape command
print(photo.shape) 

# Numpy array is mutable that means you can edit any picture without using a photo editor

photo[0][0]= [0,255,0]

# You can make your own custom photo using this concept.
# If you are in a security hacking field you can save your code in the array of the picture.
# You can crop your image using the slice operator in python.

cv2.imshow("Faizan Photo", photo[100:250 , 200:400])
cv2.waitKey()
cv2.destroyAllWindows()

# The RGB color model used for digital images, each of the three color channels(Red, Green, BLue) has a range of 0 to 255. This range represents the intensity of the color component where:0 means no intensity(none of that color) , 255 means full intensity (the maximum amount of that color).

# If you want to add a value in an array we use += operator

# a[3] += 20
# a

# Swapping is very easy in python
x = 5
y = 10

x , y = y , x

#If else statement in python

# The if-else statement is used in python to perform different actions based on different conditions.

seat = 500
if seat >= 200 : print("show the movie to all")
else: print("sorry we wont go")

# We can print both if and else statement at the same time in python.

if (print("linux")):
    print("Linux")
else:
    print("duniya")

