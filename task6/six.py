# An Algorithm is a systematic set of steps or rules used to solve a problem or perform a task.

#def faizanSirKiChai():
#    pan : 1 milk, no water
#    boil
#    tea beans
#   ginger
#   elachi
#   pepper
#   15 min stir
#   add 1 spoon sugar
#   mint


# The above code can be considered as an algorithm.
# The function faizanSirKiChai() defines a recipe for making Faizan Sir tea.
# This Function shows a clear and resuable way to organize the steps needed to make this specific type of tea.



#def faizanSirKiChai():
#   print("pan: 1 milk, no water")
#   print("15 min stir")
#   print("add 1 spoon sugar")

#faizanSirKiChai()

# A function executes its defined instructions, Like calling faizanSirKiChai() to print the steps for maing tea, it is know as function calling.

# If you were to write only faizanSirKiChai it would display <function __main__.vimalSirkiChai()>. This indicates that faizanSirKiChai is a fucntion defined in current module(__main__), but it hasn't been excuted or called to perform its specific task of printing the tea-making instructions.

#def faizanSirKiChai(t):
#   print("pan: 1 milk, no water")
#   print(t)
#   print("add 1 spoon sugar")

#faizanSirKiChai()

# Now from above if we make a variable(t) in function (t is known as time), it is known as function parameter or function input.

# But if we forgot to tell it the time it will give error.



#def faizanSirKiChai(t):
#   print("pan: 1 milk, no water")
#    print(t)
#   print("add 1 spoon sugar")

#faizanSirKiChai(30)



# Now if we want to run the code we need to give input for example 30, so it will boil for 30 mins, the input 30 that we give can also be known as an argument.

# If we give a data it needs a variable to store that data for example (t) (variable is also known as parameter)



#x = 5
#print(f"hello {x}")


# An f-string or keyword is way to create strings that can include variables or expression inside them.
# We can use the f keyword at the beginning of a string, followed by {} braces where you put the variable or expression you want to include.
# When Python sees an f-string it evaluates what's inside the {} braces and puts the result directly into the string.
# This makes it easier and more readable to combine text and values dynamically.
# to print a variable value in the middle of string, you can use string interpolation. This means inserting the variable value directly into the string.


#def faizanSirKiChai(t, s):
#    print("pan: 1 milk, no water")
#    print(t)
#    print(f"add {s} spoon sugar")


# Lets say we want to add another variable name s which will tell how much spoon sugar is required.
# In above code {s} is variable and "add spoon sugar" is strings


#faizanSirKiChai(2,5)


# Here , 2 is the first variable and 5 is second variable.

#def faizanSirKiChai(totalboiltime, SpoonAdded, milkPacket=1):
#   print(f"pan: 1 {milkPacket}, no water")
#   print(f"boil time {totalboiltime}")
#   print(f"add {SpoonAdded} spoon sugar")

# If you put a value in a variable for example, milkPacket = 1 instead of just milkpacket then its value will be fixed now it won't change when you call the function.
# Some times you give codes to other members of the company , they might not know about what a particular function do, so we will give the function some better names which will tell us what it is for.

 
#faizanSirKiChai(totalboiltime=20, SpoonAdded=1, milkPacket=1)


# An argument or variable that is passed to a function based on its position or order in the function call is known as positional argument. When you call a function, positional arguments are matched to the function's parameters in the order they are given.
# Here in above code , milkPacket ,SpoonAdded, totalboiltime is a parameter of the function faizanSirkiChai. When you call this function, you need to provide an argument for parameter. It is a positional argument because it is passed to the function based on its position in the function call.

#hand = faizanSirKiChai(totalboiltime=20, SpoonAdded=1, milkPacket=1)

#print(hand)

#Now if we add hand variable here it is not showing anything
# It is because it has no value in datatype.

def faizanSirKiChai(totalboiltime, SpoonAdded, milkPacket=1):
    print(f"pan: 1 {milkPacket}, no water")
    print(f"boil time {totalboiltime}")
    print(f"add {SpoonAdded} spoon sugar")
    return "final cup of tea"

# To print function job is to print anything which is written in print fucntion but you cant use what it is printing anywhere as function because it does not know how to send or put data in a variable.

# So all you need to do is add return function it is used to exit the function and optionally send value back to the caller.

hand = faizanSirKiChai(totalboiltime=20, SpoonAdded=1, milkPacket=1)

print(hand)

# You can use a function output or send it to variable when it return something, if you dont return then by default its return becomes none.

def lwsum(x,y):
    z = x + y
    return(z)

h = lwsum(2,5)

print(h)

# Now in the above function  if we use print function for z variable , we won t be able to store output in z , so to store the output in the z variable we will use return function.

def lwsum(x,y):
    z = x + y
    return(z)
    return("hi")

h = lwsum(2,5)
print(h)

# Here you can see the value was stored in the variable ,so you can use that stored value to print or to do anything else.

# If you apply return two times it will only return first value not second.

# Function takes input to do something and in last function gives an output.
# x,y,z,  all these are examples of input.
# To take output we use return keyword.
# Whatever you do a function output will always be one it will never be two, a function always return one thing or value.




