# Suppose we need a visitor form. We can create a class for that like this-

class VisitorForm:
    name = None
    phone = None
    email = None
    query = None

# Create an object from this class

jack = VisitorForm()
print(jack.phone)

# Whenever we run the above code a memory address is allocated on ram to store data.

# We can see that jack is not able to access phone variable because phone attribute is private

jack.phone

# Object can access function of class from outside.
# Whenever object access the function object sends its memory address to the function.

# To access a fucntion from object 
# tom.fz()

# Whenever we create a function inside a class it require a variable. Mostly this variable is self.


class VisitorFormone:
    name = None
    phone = None
    email = None
    query = None

    def fz(self):
        print("i am faizan")
        print( x.phone )

# We can also set the value from the object without hardcoding in class.

class VisitorFormSec:
    name = None
    phone = []
    email = None
    query = None
    def fz(self):
        print("i am faizan")
        print( x.phone )
    def setEmail(self, e):
        self.email = e
    def getEmail(self):
        print(self.email)

tom = VisitorFormSec()

tom.setEmail("faiz@gmail.com")
print(tom.getEmail())

# Also we can directly pass the input to the constructor. We don't need seperate methods for it.

