# I want to create a new file and add couple of lines in it
my_file_name = "resources/testfile3.txt"
my_file_handle = open(my_file_name, 'w')
my_file_handle.write("Hello Files World!")
my_file_handle.write("\n")
my_file_handle.write("Hello Files World once again!")
my_file_handle.write("\n")
my_file_handle.write("Hello Files World once again thrice!")
my_file_handle.close()

# I will open the file without the write option
fhandle = open(my_file_name)
my_file_data = fhandle.read()
for lines in my_file_data.splitlines():
    print lines

