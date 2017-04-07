# define a function named cheese_and_cracker with 2 arguments
def cheese_and_cracker(cheese_count , boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"


print "We can just give the function numbers directly:"
cheese_and_cracker(20,30) # use number as arguments passing in the function

print "OR, we can use variables from our script:"
amount_of_cheese = 10  # define variable and assign 10 to it 
amount_of_crackers = 50 # define variable and assign 50 to it

cheese_and_cracker(amount_of_cheese,amount_of_crackers) # passing the 2 variables as arguments in function



print "We can even do math inside too:"
cheese_and_cracker(10+20 , 5+6) # use math expression as arguments


print "And we can combine the two,variables and math:"
cheese_and_cracker(amount_of_cheese + 100 , amount_of_crackers + 1000) # use Mixed math expression as arguments

# lianxi-----------------------------------------------------

def study_drill(arg1,arg2):
    print "this is arg1: %r" % arg1
    print "this is arg2: %r" % arg2

a1 = int(raw_input("define variable a1:"))
a2 = int(raw_input("define variable a2:"))
study_drill(a1,a2)

study_drill(10,20)

study_drill(a1+10,a2+10)

study_drill(a1+a2,a1-a2)

study_drill(a1*2,a2/2)