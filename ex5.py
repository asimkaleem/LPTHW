# - - coding: utf- 8 - -#
# exercise around "format string"
# Format strings are string with variables embeded in them
# You embed variables inside a string by using specialized format sequences
# and then putting the variables at the end with a special syntax that tells Python, Hey, this is a
# format string, put these variables in there.

name = "Asim Kaleem Khan"
age = 42  # not a lie
height = 64  # inches
height_in_feet = round((height / 12.00))

weight = 210  # lbs
eyes = 'Brown'
teeth = 'Yellowish White'
hair = 'Black'
print "Let's talk about %s." % name
print "Printing name using  %r." % name

print "He's %d inches tall." % height
print "He's %r feet tall." % height_in_feet
print "Height in feet: ", height_in_feet
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth
# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
# Changed variable names from my_* by removing "my_" using search and replace facility of IDE
