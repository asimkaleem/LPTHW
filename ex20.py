# Function and Files
#  importing the argv
from sys import argv

# packing the arguments
script, input_file = argv

# defining print all fnc which will read the whole file
def print_all(f):
    print f.read()

# defining rewind function which uses seek method of file object which in actual sets
# offset of read write pointer within the file

def rewind(f):
    f.seek(0)


def print_a_line(line_count, f):
    print line_count, f.readline()


current_file = open(input_file)
print "First Let's print the whole file\n"
print_all(current_file)

print "Lets rewind kind of like a tape!\n"
rewind(current_file)

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)



