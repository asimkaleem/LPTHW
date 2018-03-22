
# The argv is the argument variable a very standard name in programming that you will find
# used in many other languages. This variable holds the arguments you pass to your Python script
# when you run it.

from sys import argv

script, first, second, third = argv
print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "Hello world"