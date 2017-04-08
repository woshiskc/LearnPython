from sys import argv
# unpack 2 arguments
script, input_file = argv
# difine function print_all which has 1 argument f. then print the content by f.read()
def print_all(f):
    print f.read()
# define function for set the point to starting point
def rewind(f):
    f.seek(0,0)
    #f.seek(0,1)
    #f.seek(0,2)
# define function with 2 arguments, then print arg1 , read a line of f file.
# line_count is a paramter
def print_a_line(line_count, f):
    print line_count, f.readline()

#----------------------------------------------
# make a variable named current_file , assign it to open(input_file)
current_file = open(input_file)

print "First let's print the whole file:\n"
# print all content form current_file
print_all(current_file)

print "Now let's rewind , kind of like a tape."
# set the reading file point to the starting point of the file
rewind(current_file)

print "Let's print three lines:"
# print current_file line by line
current_line = 1
print_a_line(current_line, current_file)

#current_line = current_line + 1
current_line += 1
print_a_line(current_line, current_file)

#current_line = current_line + 1
current_line += 1
print_a_line(current_line, current_file)

# after operating file , close them
current_file.close()
