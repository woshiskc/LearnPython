# -*- coding: utf-8 -*-
print "How old are you?" ,
age = raw_input()
print "How tall are you?" ,
height = raw_input()
print "How much do you weight?",
weight = raw_input()

print "test1"
test1 = raw_input("input some words:")
print test1
print "%r"% test1
print "%s"% test1

# if I use %s instead %r , the strings are without ''
print "So , you 're %r old , %r tall and %r heavy." % (age , height , weight)
print "So , you 're %s old , %s tall and %s heavy." % (age , height , weight)
