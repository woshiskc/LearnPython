# 提出问题 #

----------

是时候加快速度了。你已经做了大量打印简单东西的练习。但是那些简单的玩意真的十分无聊。我们接下来要做的事情是要把数据加入到程序当中。这有点点棘手，因为你必须学做2件你不一定马上能弄懂的事情。但请相信我，在几个练习之后你会掌握他们。

多数软件是这么工作的：
1. 接收用户的输入
2. 处理输入
3. 打印结果

你已经打印了很多字符串，但是你还不能从用户那里获取任何输入。你也许不清楚什么是`input`，准确地打印下面的代码，在下个练习中，我们将解释什么是`input`

我们在每一个`print`函数后面加了`，`(逗号)。这样的话`print`下面的函数就不会另起一行了。

## 练习 ##
- 上网去查`python`中的`raw_input()`是干嘛的
- 你能找到其他使用它的方式吗？试一试你找到的例子
- 找一些其他的问题并以这样的形式写下来
- 与转义序列相关的问题，试着弄明白为什么最后一行`'6\'2"' `中带有` \'`。想想有什么方法能隐藏单引号从而避免它被识别为一个字符串

## 问答 ##
**我怎么样从其他人那里获取数字，并且能够让我运用到运算中？**

这个问题有点深。试着用`x = int(raw_input())`，先以字符串的形式从`raw_input()`中获取数字，然后用`int()`将其转化为整型变量

**为啥我这样输入了我的身高`raw_input("6'2")`，但是不起作用？**

不能将身高直接输入，首先像我写的那样写下代码。然后再运行，当光标暂停时，用键盘输入身高数值。

**为啥在第八行你分行了？**

每行不超出80个字符的长度，这个是`python`程序员喜闻乐见的约定俗成。你可以输出成一行如果你愿意的话

**`input()`和`raw_input()`的区别？**

这两个函数均能接收字符串 ，但`raw_input()`直接读取控制台的输入，返回字符串类型。而对于 `input()`，它希望能够读取一个合法的`python`表达式，即你输入字符串的时候必须使用引号将它括起来，否则它会引发一个SyntaxError。
作者说`input()`有安全性问题，所以应该忽略他

**为什么当我的字符串打印出来后，前面带了个`u`，像这样`u'35'`？**

`python`告诉你这个字符串采用了`Unicode`编码。使用`%s`格式化字符串能解决这个问题。
