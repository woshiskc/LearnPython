# -*- coding: utf-8 -*-
#定义变量cars，赋值100
cars = 100
#定义变量space_in_a_car,赋值4.0 浮点型
space_in_a_car = 4.0
#定义变量drivers，赋值30
drivers = 30
#定义变量passengers,赋值90
passengers = 90
#定义变量cars_not_driven,赋值为cars - drivers
cars_not_driven = cars - drivers
#定义变量cars_driven，赋值为driven
cars_driven = drivers
#定义变量carpool_capacity ,赋值为cars_driven * space_in_a_car
carpool_capacity = cars_driven * space_in_a_car
#定义变量average_passengers_per_car，赋值为passengers / cars_driven
average_passengers_per_car = passengers / cars_driven


print "There are" , cars , "cars available."
print "There are only",drivers,"drivers available."
print "There will be",cars_not_driven,"empty cars today."
print "We can transport",carpool_capacity,"people today."
print "We have",passengers,"to carpool today."
print "We need to put about",average_passengers_per_car,"in each car."
print "Hey %s there." % "you"

#do some test
#test1 = 5
print test1
test1 = 10
print test1
