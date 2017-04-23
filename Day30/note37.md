# 37 复习符号
-----------------------
是时候复习一下符号和python关键词了。尝试看一些新的字符和关键词，为后面的课程做准备。我将所有重要的python关键词和符号写了出来，供学习

这一课中，先凭记忆将每一个关键词的作用写下来。接下来上网查这些关键词，验证他们的作用。有些词不是那么容易搜到，尽最大努力去做

如果你记错了某一个。那么做一个卡片记录正确的定义。然后重新学习它

最后，使用这些符号和关键词写一个小程序。目的是掌握他们的用法。

## Keywords-关键词

|Keyword	|Description|	Example|
|-----------|-----------|----------|
|and	|Logical and.|	True and False == False|
|as|	Part of the with-as statement.|	with X as Y: pass|
|assert	|Assert (ensure) that something is true.	|assert False, "Error!"|
|break	|Stop this loop right now.	|while True: break|
|class	|Define a class.	|class Person(object)|
|continue	|Don't process more of the loop, do it again.|	while True: continue|
|def	|Define a function.|	def X(): pass|
|del	|Delete from dictionary.	|del X[Y]|
|elif	|Else if condition.	|if: X; elif: Y; else: J|
|else	|Else condition.	|if: X; elif: Y; else: J|
|except	|If an exception happens, do this.	|except ValueError, e: print e|
|exec	|Run a string as Python.	|exec 'print "hello"'|
|finally	|Exceptions or not, finally do this no matter what.	|finally: pass|
|for	|Loop over a collection of things.	|for X in Y: pass|
|from	|Importing specific parts of a module.	|from x import Y|
|global	|Declare that you want a global variable.	|global X|
|if	|If condition.	|if: X; elif: Y; else: J|
|import	|Import a module into this one to use.	|import os|
|in	|Part of for-loops. Also a test of X in Y.	|for X in Y: pass also 1 in [1] == True|
|is	|Like == to test equality.	|1 is 1 == True|
|lambda	|Create a short anonymous function.	|s = lambda y: y ** y; s(3)|
|not	|Logical not.	|not True == False|
|or	|Logical or.	|True or False == True|
|pass	|This block is empty.	|def empty(): pass|
|print	|Print this string.|print 'this string'|
|raise	|Raise an exception when things go wrong.	|raise ValueError("No")|
|return	|Exit the function with a return value.	|def X(): return Y|
|try	|Try this block, and if exception, go to except.	|try: pass|
|while	|While loop.	|while X: pass|
|with	|With an expression as a variable do.	|with X as Y: pass|
|yield	|Pause here and return to caller.	|def X(): yield Y; X().next()|


## Data Types 数据类型

|Type	|Description	|Example|
|-------|---------------|-------|
|True	|True boolean value.	|True or False == True|
|False	|False boolean value.	|False and True == False|
|None	|Represents "nothing" or "no value".	|x = None|
|strings	|Stores textual information.	|x = "hello"|
|numbers	|Stores integers.	|i = 100|
|floats	|Stores decimals.	|i = 10.389|
|lists	|Stores a list of things.	|j = [1,2,3,4]|
|dicts	|Stores a key=value mapping of things.	|e = {'x': 1, 'y': 2}|


## String Escape Sequences 转义字符序列

|Escape	|Description|
|-------|-----------|
|\\	|Backslash|
|\'	|Single-quote|
|\"	|Double-quote|
|\a	|Bell|
|\b	|Backspace|
|\f	|Formfeed|
|\n	|Newline|
|\r	|Carriage|
|\t	|Tab|
|\v	|Vertical tab|


## String Formats 格式化字符

|Escape	|Description	|Example|
|-------|--------------|--------|
|%d	|Decimal integers (not floating point).	|"%d" % 45 == '45'|
|%i	|Same as %d.	|"%i" % 45 == '45'|
|%o	|Octal number.|	"%o" % 1000 == '1750'|
|%u	|Unsigned decimal.	|"%u" % -1000 == '-1000'|
|%x	|Hexadecimal lowercase.	|"%x" % 1000 == '3e8'|
|%X	|Hexadecimal uppercase.	|"%X" % 1000 == '3E8'|
|%e	|Exponential notation, lowercase 'e'.	|"%e" % 1000 == '1.000000e+03'|
|%E	|Exponential notation, uppercase 'E'.	|"%E" % 1000 == '1.000000E+03'|
|%f	|Floating point real number.	|"%f" % 10.34 == '10.340000'|
|%F	|Same as %f.	|"%F" % 10.34 == '10.340000'|
|%g	|Either %f or %e, whichever is shorter.	|"%g" % 10.34 == '10.34'|
|%G	|Same as %g but uppercase.	|"%G" % 10.34 == '10.34'|
|%c	|Character format.	|"%c" % 34 == '"'|
|%r	|Repr format (debugging format).	|"%r" % int == "<type 'int'>"|
|%s	|String format.	|"%s there" % 'hi' == 'hi there'|
|%%	|A percent sign.	|"%g%%" % 10.34 == '10.34%'|


## Operators 运算符

|Operator	|Description	|Example|
|------------|------------|-------|
|+	|Addition	|2 + 4 == 6|
|-	|Subtraction	|2 - 4 == -2|
|*	|Multiplication	|2 * 4 == 8|
|**|	Power of	|2 ** 4 == 16|
|/	|Division	|2 / 4.0 == 0.5|
|//	|Floor division	|2 // 4.0 == 0.0|
|%	|String interpolate or modulus|	2 % 4 == 2|
|<	|Less than	|4 < 4 == False|
|>	|Greater than	|4 > 4 == False|
|<=	|Less than equal	|4 <= 4 == True|
|>=	|Greater than equal	|4 >= 4 == True|
|==	|Equal	|4 == 5 == False|
|!=	|Not equal|	4 != 5 == True|
|<>	|Not equal	|4 <> 5 == True|
|( )	|Parenthesis	|len('hi') == 2|
|[ ]	|List brackets	|[1,3,4]|
|{ }	|Dict curly braces	|{'x': 5, 'y': 10}|
|@  |At (decorators)	|@classmethod|
|,	|Comma	|range(0, 10)|
|:	|Colon	|def X():|
|.	|Dot	|self.x = 10|
|=	|Assign equal	|x = 10|
|;	|semi-colon	|print "hi"; print "there"|
|+=	|Add and assign|	x = 1; x += 2|
|-=	|Subtract and assign	|x = 1; x -= 2|
|*=	|Multiply and assign	|x = 1; x *= 2|
|/=	|Divide and assign|	x = 1; x /= 2|
|//=	|Floor divide and assign	|x = 1; x //= 2|
|%=	|Modulus assign	|x = 1; x %= 2|
|**=	|Power assign	|x = 1; x **= 2|

**花费一周的时间。记住所有的符号。并做检查。没记住的，继续学习，强化记忆**


## 读代码

现在你可以找一些python代码来读了。你应该读那些你能从中获取想法和理念的。你应该有足够的知识去阅读，但可能会不明白这些代码是做什么的。这一课的目的就是利用你学的东西，去理解其他人写的代码的含义。

首先，打印出你想了解的代码。是的，打印出来。因为你的眼和脑会更多的阅读纸上的内容。

然后。读代码，将下列项进行记录：

1. 函数以及他们的用法和作用
2. 每一个变量何时第一次被赋值
3. 重名的变量。
4. 没有else的if条件判断。他们正确吗？
5. 永久循环的while-loop
6. 任何一段你看不懂的代码

第三。一旦你将所有符合要求的地方都标记完成。试着写注释。解释函数用途，涉及的变量有哪些，说明任何你能解释这段代码的部分。

最后。在所有难理解的部分上，通过打印变量值的方式做变量跟踪，一行一行的。一个函数一个函数的。

如果你对怎样写代码有更好的注意。去电脑上重读他看看能不能发现新的东西。持续读更多代码，直到你不需要打印、跟踪任何东西


## 练习

1. 理解什么是流程图。画一些出来
2. 如果发现代码中的错误，修正他。并且将这个修改告诉代码的原作者
3. 另一种学习方法是为你笔记上的代码写注释。有些时候这些注释会帮助其他看这段代码的人。

