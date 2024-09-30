import os



print("\t\t\t\Welcome to Menu Tools")
print("\t\t\t\----------------------")

print("""
    press1: to open notepad
    press2: to open chrome
    press3: to open VLC
    press4: to open whatsapp

""")







ch = input("Enter your choice: ")
print(ch)

if (("notepad" in ch) or (editor in ch)) and (not("dont"in ch)):
    os.system("notepad")
elif int(io) ==2:
    os.system("chrome")
elif int(io) ==3:
    os.system("vlc")
else:
    print("idk")

# In above code you can see that  (("notepad" in ch) or (editor in ch)) and (not("dont"in ch)) it checks if the user's input contains either "notepad" or "editor" and ensure that the input does not contain the word "dont".

# If the user enters a command that includes "dont" such as "dont open notepad", the condition (not("dont" in ch)) evaluates to false. Therefore overall condition evalautes to false.

# As a result the program executes the else block and prints "Command not recognized or prohibited"

# It is useful in ensuring that only valid and intended actions are excuted based on the user's input.

# ELIF 
# elif allows subsequent condition to be evaluated in sequence. This feature is particularly useful when you need to check multiple condition in a structured manner without nestin=g numerous if statements.

# Here elif is used to enhance code clarity and origanization where each condition can be isolated and addressed seperately.

# IMPORT OS

# The import os statement in python is used to access operating system functionalities and feature through the os module. this module provides a wide range of methods that allow python programs to interact with the operating system.

# In which os.system() is a function from the os that allows you to execute shell commands or system commands directly from within a Python script.

# IN KEYWORD

# The in keyword is used to check for the existence of a value within a sequence or collection. It is primarily employed in conditional statements, loops, and comprehensions to determine if a specified elements is present in a string, list, tuple, dictionary keys, or other iterable objects.

if linux in s:
    print("ok")
else:
    print("not")

# As you can see in above image "Linux" in s: demonstartes the use of the in keyword in python to check if the substrings "linux" exits within the string varaible s. If "Linux" is found within s, the condition evaluates to True and the statement print("ok") is excuted, indicated that "linux" is present in the string. 
