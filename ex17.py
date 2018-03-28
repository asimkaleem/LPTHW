from sys import argv
from os.path import exists

script, from_file, to_file = argv
print "Copying from %s to %s: " %(from_file, to_file)

# we should do these two on one line too, how?

in_file = open(from_file)
in_data = in_file.read()

print "This input file %d bytes long: " % len(in_data)
print "Does the output file exists? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL- C to abort."
print "Copying content..."
raw_input()
out_file = open(to_file, 'w')
out_file.write(in_data)
print "Alright, all done."
out_file.close()
in_file.close()
