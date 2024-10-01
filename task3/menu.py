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

if (("notepad" in ch) or ("editor" in ch)) and (not("dont"in ch)):
    os.system("notepad")
elif (ch) ==2:
    os.system("chrome")
elif (ch)==3:
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
s = "hey"
if "linux" in s:
    print("ok")
else:
    print("not")

# As you can see in above image "Linux" in s: demonstartes the use of the in keyword in python to check if the substrings "linux" exits within the string varaible s. If "Linux" is found within s, the condition evaluates to True and the statement print("ok") is excuted, indicated that "linux" is present in the string.

# Also in above code,  (("notepad" in ch) or ("editor" in ch)) and (not ("dont" in ch)) utilizea the in kwyword in Python for checking substring membership within the string variable ch.

# Its usage are: This expression evaluates to True if either the substrings "notepad" or "editor" is found within the string ch, and simultaneously ensures that the substring "dont" is not present in ch. It combines logical operation (and , or, not) with substrings checks using in.

# LOGICAL OPERATORS

# logical operators (and,or,not) are used to combine and evaluate multiple condition in a single expression

time = 9
seat = 300
print(time> 8 and seat >= 200)

# The AND operator in python is used to combine multiple condition, ensuring that all conditions must be true for the entire expression to evalauted to true. If any condition is false the combined expression evaluates to false. This is useful for scenarios where multiple criteria must all be met.

# In above code this expression checks if both condition are true: time is greater than 8 and seat is greater that equal to 200.

# Explanation: The and operator returns True only if both conditions on its sides are True. In this case, time > 8 is true because 9 is greater than 8 and seat >= 200 is True because 300 is greater than or equal to 200. Therefore, the combined expression evalautes to True.

time = 11
seat = 30
print(time > 8 and seat >= 200)

# In above code this expression checks if both conditions are true: time is greater than 8 and seat is greater than or equal to 200.
# Explanation: The and operator returns True only if both conditions on its sides are True. In this case, time > 8 is True because 11 is greater than 8, but seat >= 200 is False because 30 is not greater than or equal to 200. Therefore, the combined expression evaluates to False.

print(not (time > 8))

# The not keyword is used to invert the boolean value of give expression. It turns into False and vice versa.

# Now in above code not (time > 8)

# Usecase: This expression negates the condition time > 8.
# The not operator inverts the booleans value of the condition. Since time > 8 is true, applying not makes it False. Therefore the expression evalautes to false.

# The OR operator in Python combines multiple codntions, where the entire expression evaluates to true if at least one condition is true. If all condition are false, the combined expression evalautes to false. This is useful for scenerios where meeting any one of multiple criteria is sufficient.

# Now time > 8 or time > 10 or time > 7
# Usecase: This expression checks if only any conditions are true: Time is greater that 8, 10 or 7.
# Explaination : The operators returns True if atleast one of the conditions is True. In this case, all conditions (time > 8, time > 10, time >7) are True because 11 is greater than 8,10 and 7. Therefore, the combines expression evaluates to True.

# LAZY OPERATOR
# The concepts of Lazy evaluation or short-circuiting primarily applies to logical operators like OR. Lazy evaluation allows you to optimize performance by evaluating expressions only as far as necessary to determine the final outcome.

u = 5
print(u > 4 or print ("yes"))

# The or operator with lazy evaluation is commonly used when you have an expression where the second operand involves a potentially expensive operation(such as a fucntion call or I/O operation)

# Python evalautes the left operand u > 4.

# Since u is 5 and 5 > 4 is True, Python does not need to evalautes the right operand(print("yes")).

# This is becasue in a logical or opration if the left operand is True, the entire expression is alredy determnined to be true, regradless of the right operand.

# Output: In this case because u > 4 is True, The expression u > 4 or print("yes") evalutes to true without executing print ("yes").

#  Truth Table is used to illustrate the output of logical operations for all possible input values. It is particularly useful for understanding how logical operators like and, or and not function.

# The Time complexity refers to the measure of how much run time does it take to run an algorithm, It is used to make informed decision about algorithemic effieceny ensuring that application and systems perform optimally even with larger datasets or more complex computations.



