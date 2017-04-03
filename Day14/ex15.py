# import argv
from sys import argv
# unpack argv with 2 argument
script, filename = argv

txt = open(filename) # open the file , and assign the file to variable txt

print "Here's your file %r:" % filename # print file name
print txt.read() # print file content
txt.close()

print "Type the filename again:"
file_again = raw_input("> ") # use inputs file name , assign name to variable file_again

txt_again = open(file_again) # open the file , and assign the file to variable txt_again

print txt_again.read() # print file content

txt_again.close()
