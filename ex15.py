# imports argv module
from sys import argv

# two arguments to unpack
script, filename = argv

# variable txt will be assigned with the file handle if the file name and path is correct
txt = open(filename)

# prints the sentence of the with file name given in argv
print "Here is the content of the %r" % filename

# content of file is read and then printed to console
print txt.read()

# command prompts appears for another file to print
file_again = raw_input("another file to print? ")

# file handle is created if correct file name is given
txt_again = open(file_again)

# content of the new file is printed
print txt_again.read()
