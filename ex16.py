# -*- encoding: UTF-8 -*-#

"""
close — Closes the file. Like File->Save.. in your editor.
read—Reads the contents of the fi le. You can assign the result to a variable.
readline—Reads just one line of a text fi le.
truncate—Empties the fi le. Watch out if you care about the fi le.
write(stuff)—Writes stuff to the file.
"""
from sys import argv

script, filename = argv
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL- C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")
print "Opening the file..."
target = open(filename, 'w')
# target = open(filename)

print "printing the current content of the file:"
print target.read()

print "Truncating the file. Goodbye!",
target.truncate()

print "Now I'm going to ask you for three to four lines ."
line1 = raw_input("line 1:> ")
line2 = raw_input("line 2:? ")
line3 = raw_input("line 3:? ")
line4 = raw_input("line 4:? ")
print "I'm going to write these to the file."
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
target.write(line4)
target.write("\n")
print "And finally, we close it."
target.close()
