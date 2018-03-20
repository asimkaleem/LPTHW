# Prints a string
print "Mary had a little lamb."

# Prints a string with embedded string formatter
print "Its fleece was white as %s." % 'snow'

# Prints a string
print "And everywhere that Mary went."

# Prints (.) 10 times
print "." * 10  # what'd that do?

# Declare a single character string variable
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. try removing it to see what happens
# concatinates first 6 single character variables created above
print end1 + end2 + end3 + end4 + end5 + end6,
# the comma at the end makes sure that next control is shifted on same line
#  therefore instead of two lines of print two words are printed in same line
print end7 + end8 + end9 + end10 + end11 + end12