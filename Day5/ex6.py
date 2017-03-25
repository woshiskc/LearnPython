#-*- coding：utf-8 -*-

#定义格式字符串变量x
x = "There are %d types of people." % 10
#定义字符串变量binary
binary = "binary"
#定义字符串变量do_not
do_not = "don't"
#定义格式字符串变量y
y = "Those who know %s and those who %s." % (binary, do_not)

#打印x文本
print x
#打印y文本
print y

#打印我说了X这句话
print "I said: %r." % x
#打印我说了Y这句话
print "I also said: '%s'." % y

#定义布尔变量hilarious，赋值False
hilarious = False
#定义格式化字符串变量joke_evaluation
joke_evaluation = "Isn't that joke so funny?! %r"
#打印格式化字符串
print joke_evaluation % hilarious

#定义字符串变量w
w = "This is the left side of..."
#定义媳妇串变量e
e = "a string with a right side."

#打印w和e合成的结果
print w + e
