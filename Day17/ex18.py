# this one is like your script with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# this function just takes one argument
def print_one(arg1):
    print "arg1 : %r" % arg1   

# this one takes no argument
def print_none():
    print "I got nothing."

print_two("skc","hahaha")
print_two_again("skc1","hahaha1")
print_one("First!")
print_none()

