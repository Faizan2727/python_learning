#to print in python we can use print() function

print("hello world")

#there are function for everything in python
#Variable are reference. To store the data and use it in the future we use variables.
x=5
print(5)
#Python has online interpreter. Also we can also use the python using IDE like jupyter notebook.


#To store multiple values in same varaible we use tuple.

db = (1111,2222,3333,4444)
print(db)

#Tuple is immutable in python

#db[6]=6666 #this will not work file will give error so i have to comment this.

#To know the data type of any variable in python we can use type function.

print(type(db))

# to make list in python use square brackets

db1 = [1111,2222,3333,4444]
print(db1)
print(type(db1))

#to add value in list
db1[2]=8888
print(db1)

#To use slice operator in python to extract data according to index last index in excluded.

print(db1[0:3]) #this slice operation retrieve elements from index 0 up to,but not including index3

print(db1[:3]) #this will show from begining of index list to 2 becoz last index is always excluded. 

print(db1[2:]) #this will show from 2 index to last.

#To create 2d array or metrices-
db3 = [
        ["faizan1", 1111, "fa1@gmail.com"],
        ["faizan2", 2222, "fa2@gmail.com"],
        ["faizan3", 3333, "fa3@gmail.com"],
]

print(db3)


#To access the elements 
print(db3[1])
print(db3[2][1])

#In python list does not support column wise operation. It only supports row wise operation.
#To do column wise operation we can use numpy array.
#Every function comes from the module. To use numpy import numpy module.

import numpy
#to convert the list to numpy use
db4 = numpy.array(db3)


#now retrieve a column use-
print(db4[ : , 1])

# to install a library in python pip cmd is used eg.
#pip install numpy

#to see the list of installed librires we use "pip list" cmd

#data is never saved in a class. It is saved in an object.

#Python has built primitive data structures.

#If we want to make our custom data structure, we need to use classes.

#to create a class in pythonuse the following code.

class VisitorFrom:
    name = None
    phone = None
    email = None
    query = None

#class VisitorFrom: This line defines a new class named VisitorForm.
# A class is a blueprint for creating objects.

#class VisitorFrom:
#    name = None
#    phone = None
#   email = None
#   query = None
#These lines define class attributes. Attributes are variables that belong to the class.In this case name,phone,email,query afre attributes of the VisitorForm class, and they are all initialized to None.

#To create a object use the following. This is called instantiation.

tom = VisitorFrom()

#To click photograph using python we use cv2 library.
#Photograph is a numpy array.
#To click an image use the code-
import cv2
cap = cv2.VideoCapture(0)
status, photo = cap.read()

#Now to views the photo use imshow-
cv2.imshow('MyWindowName', photo)
cv2.waitKey()
cv2.destroyAllWindows()

#If we check the shape of this image we get three values-

print(photo.shape)

#To release the camera we use-
cap.release()







