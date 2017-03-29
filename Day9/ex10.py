# -*- coding: utf-8 -*-
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
j = 1

fat_cat = """
I will do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

fat_cat2 = '''
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''


print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print fat_cat2

while j<3:
    for i in["/","-","|","\\","|"]:
        print "%s\r" % i,
        j = j+1
