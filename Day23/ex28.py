
test1 = (1 == 1 and 2 == 1)
test2 = (True and True)
test3 = (False and True)
test4 = (1 == 1 and 2 == 1)
test5 = ("test" == "test")
test6 = (1 == 1 or 2 != 1)
test7 = (True and 1 == 1)
test8 = (False and 0 != 0)
test9 = (True or 1 == 1)
test10 = ("test" == "testing")
test11 = (1 != 0 and 2 == 1)
test12 = ("test" != "testing")
test13 = ("test" == 1)
test14 = (not (True and False))
test15 = (not (1 == 1 and 0 != 1))
test16 = (not (10 == 1 or 1000 == 1000))
test17 = (not (1 != 10 or 3 == 4))
test18 = (not ("testing" == "testing" and "Zed" == "Cool Guy"))
test19 = (1 == 1 and (not ("testing" == 1 or 1 == 0)))
test20 = ("chunky" == "bacon" and (not (3 == 4 or 3 == 3)))
test21 = (3 == 3 and (not ("testing" == "testing" or "Python" == "Fun")))

print """
%r
%r
%r
""" % (test21,test14,test1)
