# Your Name Here
#
# The purpose of this piece of code is to demonstrate 
# the input function which allows a coder to create
# programs that lets users input code
#
import random 

print("Hello we will need some basic information")
print("Please input your name ")

# Here we create a function name input and assign it a variable 
# Designated as name

name = input(); 

# In this line we output name to the screen
print("Hello I'M " + name +"!")

# Here is another example 
# Note that instead of printing multiple lines we give the question to be asked as
# an argument for a pararmeter accepted by input
age = input("Well, how old are you?: ")

# Output the user info
print("Howdy " + name + " so I heard your " + age)
print("But someone at the office told me your really " + str(random.randint(0,100)))

#
# Here is some additional links if you want to read more on getting user input
# https://www.w3schools.com/python/python_user_input.asp
# https://docs.python.org/3/tutorial/inputoutput.html