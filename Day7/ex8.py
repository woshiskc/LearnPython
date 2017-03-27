# -*- coding: utf-8 -*-

# define formatter . assign a format string to formatter
formatter = "%r %r %r %r"
test = "%r %r" # "%s %s"


print formatter % (1,2,3,4) # the variables of formatter are numbers
print formatter % ("one", "two", "three", "four") # the variables of formatter are strings
print formatter % (True, False, False, True) # the variables of formatter are Keywords
print formatter % ("Ture","False","Ture","False")
print formatter % (formatter, formatter, formatter, formatter)  # the variables of formatter are
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)

print formatter % ("hi","你好","goodbye","再见")
print test % ("hi","你好")#.decode('utf-8').encode('gbk'))
