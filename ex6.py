# --coding: utf-8 --
# Python knows you want something to be a string when you put either
# " (double-quotes) or ' (single- quotes) around the text
# Creating a string and also using string formating to induce a digit in that string
x = "There are %d types of people." % 10

# Creating a string variable named "binary"
binary = "binary"

# Creating string variable named "do_not"
do_not = "don't"

# Creating a string variable with two string format induced in it
# string with in string
y = "Those who know %s and those who %s." % (binary, do_not)

# printing the x variable
print x

# printing the y variable
print y

# Printing the string with string formater for r which means what ever is needed can be entered
# string with in string
print "I said: %r." % x

# Print a string with string formater in it
# string with in string
print "I also said: '%s'." % y

# creating new variable
hilarious = False

# creating a string variable
joke_evaluation = "Isn't that joke so funny?! %r"

# printing the variables defined above and inducing a string formatter in it
# string with in string
print joke_evaluation % hilarious

# declaring a string variable
w = "This is the left side of..."

# declaring a string variable
e = "a string with a right side."

# string concatination
print w + e
