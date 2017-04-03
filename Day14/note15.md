# 读取文件
-------------
你已经了解怎么使用`raw_input`和`argv`获取用户输入。现在你将学习如何读取文件。你将通过这个练习理解其中的原理。所以请仔细做练习，记得检查。操作文件是很危险的事，如果你不够小心，就会清除文件，丢失你之前做过的工作。

这个练习涉及写入2个文件。一个是`ex15.py`。一个是`ex15_sample.txt`，这个文件不是脚本，它是一个文本文件，将会被我们写的脚本读取内容。下面是这个文件的内容：

>This is stuff I typed into a file.<BR>
>It is really cool stuff.<BR>
>Lots and lots of fun to have in here.

我们要做的事情是，使用脚本打开这个文件，并且在屏幕上打印出来。但是我们不想让`ex15_sample.txt`这个名字在脚本中是一个硬编码。这样做很糟糕，因为我们还想加载其他的文件。解决方式就是使用`argv`或者`raw_input`去询问用户打开什么文件，而不是直接定死打开文件的名字。

>from sys import argv
>
>script, filename = argv
>
>txt = open(filename)
>
>print "Here's your file %r:" % filename
>print txt.read()
>
>print "Type the filename again:"
>file_again = raw_input("> ")
>
>txt_again = open(file_again)
>
>print txt_again.read()

## 新命令
**open**<BR>
常见格式为：
open(文件路径+文件名，打开模式)

**read**<BR>
`read()`是读文件的方法，括号内填入要读取的字符数。不填数字表示读取全部内容

以上为最基本的内容。`open`和`read`可以附带各种参数。

## 练习
1. 为每一行写注释
2. 试着搜索`open`函数用法
3. 课文中的命令指的就是函数和方法。晚些时候会学到
4. 去掉10-15行然后运行脚本
5. 只使用`raw_input`，然后尝试运行脚本，为啥使用一种方式获取文件名比另一种好。
6. 打开`python`使用`open`函数，看他是怎么读取文件的
7. 对`txt`和`txt_again`变量使用`close()`函数，对文件执行完操作后，关闭文件十分重要