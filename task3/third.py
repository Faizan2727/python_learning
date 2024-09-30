# Use the cd function to change thr current working directory in various command-lines interfaces and programming enviroments.

print("\t\t\t\Welcome to Menu Tools")
print("\t\t\t\----------------------")

print("""
    press1: to open notepad
    press2: to open chrome
    press3: to open VLC
    press4: to open whatsapp

""")

# Statement
# Statement in python are fundamental units of code that instruct the interpreter to perform specifc actions or operations. Like input / output operation (input,print)

x = "this is new\n here we go"
print(x)

# Each statement typically ends with a newline character but can span multiple lines using blackslahes \ for continuation

# Mutiline string in python is string that spans multiple lines. It can be created using quotes("""or''') helps in improving the readability of code by keeping long text blocks intact and easy to manage. enhancing the overall clarity and functionality of the code.

# Input Function

# When input() is called, the program execution paues and waits fotr the user to type something. The entered data is then returned as astring, which can be stored in variable for further processing.


a = 5 
print(a)

a = input()
print(a)

# Suppose we want to handle input form the user and output to the concole.

b = input("Enter you choice: ")
print(b)

# So we can use the input() fucntion here use it to prompt the user to enter data, which is then captured as a string and stored in a variable.

# This function can be used for various purpose like  data collection user communication and interactive experiences.

# The above code what is type in input is known as prompt. The input() The prompt is essential in interactive program where user input is required. It guides the user on what kind of information they need to provide.

# IF ELSE

# The if-else conditional statement allows multiple condtions to be checked in sequence, providing a way to handle different scenerios with corresponding code.

ch = input("Enter your choice: ")
print(ch)

if ch == 1:
    print("notepad")
else:
    print("idk")

# In this case since ch is not 1 the output will be idk. This demonstrates the basic usage of if and else statement for simple conditional checks in python.

# This construct is useful when you need to perform different actions based on a single condition.

# MENU PR0JECT
# A python menu is created to provide user with a structured interface where they can ineteractively choose from various functionalities or optons offered by a program.

import os

io = input("Enter your choice: ")
print(io)

if int(io) == 1:
    os.system("notepad")
elif int(io) ==2:
    os.system("chrome")
elif int(io) ==3:
    os.system("vlc")
else:
    print("idk")

# You can add as many fucnton as possible in the menu.

