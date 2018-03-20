# - - coding: utf- 8 - -#
# exercise around "format string"
# Format strings are string with variables embeded in them
# You embed variables inside a string by using specialized format sequences
# and then putting the variables at the end with a special syntax that tells Python, Hey, this is a
# format string, put these variables in there.

my_name = "Asim Kaleem Khan"
my_age = 42  # not a lie
my_height = 84  # inches
my_weight = 210  # lbs
my_eyes = 'Brown'
my_teeth = 'Yellowish White'
my_hair = 'Black'
print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth
# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)
