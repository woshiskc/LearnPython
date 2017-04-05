from sys import argv

script,filename = argv

print "we are going to erase %r ." % filename
print "If you don't want that ,hit CTRL-C(^C)."
print "If you do want that,hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename,'w') # make sure you have right to write on the disk ,or you will get IOError 13



print "Truncate the file .Goodbye!"
target.truncate()

print "Now I am going to ask you for three lines."
line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")

# study drill
totalline = """
%s
%s
%s
""" % (line1,line2,line3)

print "I am going to write these to the file."

#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")
target.write(totalline)

print "And finally , we close it."
target.close()


