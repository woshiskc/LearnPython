# 输出 输出 输出 #

----------

这本书的模式：通过许多例子去教你学习新东西。直接从代码开始你可能不明白，后面不断的练习可以帮助你理解。如果现在你仍旧不理解某些东西。你接下来需要去完成更多的练习。记录下你不懂的内容，继续学习。

## 练习 ##
检查作业，写下自己的错误。避免下次再犯。

## 问答 ##
**为什么`\n`换行在我使用`%r`时就不起作用了？**<br>
这和`%r`的工作原理相关。`%r`就是`repr()`,`repr`就是对`string`的一个格式化处理，即，返回的是一个格式化处理过的`string`（新对象）.在某些时候，`%r`的结果和`%s`结果相同，比如对象是int型。`%s`输出的结果一般是给用户看的。`%r`则用于调试

**为什么我在三个双引号间加空格会报错**<BR>
必须写成`"""`而不是`" " "`，意味着每一个双引之间都不能有空格。<BR>在定义变量的时候，也可以用`"""`。效果同直接打印`"""`中的分行的字符串。
比如：<br>
>print """<br>
There's something going on here.<br>
With the three double-quotes.<br>
We'll be able to type as much as we like.<br>
Even 4 lines if we want, or 5, or 6.<br>
"""<br>


和<br>
>text = """There's something going on here.<br>
With the three double-quotes.<br>
We'll be able to type as much as we like.<br>
Even 4 lines if we want, or 5, or 6.<br>
"""<br>

>print text<BR>

结果是一样的

**太糟糕了，我经常犯拼写错误**<BR>
常见的程序上的错误都是一些拼写错误、简单的语法错误。要细心！细心再细心

## 其他 ##
集中时间学习git使用。掌握添加、删除、更新等基本功能