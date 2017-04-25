# 38 对列表进行操作
----------------------------
你已经学习了列表。当你在学习`while-loop`循环时，你将数字加入到列表末尾，并将列表打印出来。之前的某个练习也要求你查找文档，学习所有和列表相关的函数。如果你不明白我在说什么，你可以回顾一下之前学过的内容。

找到了？记住了？很好。当你做完了这些工作，你就有一个列表了。然后你对列表使用`append`函数，你可能不太明白发生了什么，所以，继续看我们能对列表做什么。

当你写下`mystuff.append('hello')`。你其实已经调用了python中的一个事件，这个事件发生在`mystuff`列表上。下面来说说他们是怎么工作的：

1. Python看到你提到`mystuff`，它会查找该变量。它可能必须向前查看你是否使用 `=` 去创建了（mystuff），看它是否是函数参数，或者全局变量。以上任何方式都必须先找到`mystuff`

2. 一旦找到了`mystuff`。python会读后面的`.`操作符。然后看`mystuff`中的变量。从`mystuff`是一个表开始，它就知道`mystuff`有一堆功能函数。

3. 然后它接触到`append`，然后对比所有`mystuff`声明是自己的变量名字。如果`append`包含在里面，那么python将会抓取它。

4. 下一步，python看到了`( `然后意识到，“嘿，这应该是一个函数。”从这儿，它像往常一样调用(运行，执行)这个函数。但是不一样的是它是带特殊参数的调用

5. 这个特殊的参数就是：`mystuff`！这很奇怪，对吧。但这就是python工作的方式，最好记住它。发生了什么呢？总结一下就是，以`append(mystuff, 'hello') `的调用函数方式替代了 你读到的`mystuff.append('hello') `这种调用方式。


在很多地方，你不需要知道这些。但是它将会很有帮助，如果你在python中得到了下面的报错信息：

```py
 python
Python 2.6.5 (r265:79063, Apr 16 2010, 13:57:41)
[GCC 4.4.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> class Thing(object):
...     def test(message):
...             print message
...
>>> a = Thing()
>>> a.test("hello")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: test() takes exactly 1 argument (2 given)
>>>
```

上面那些代码是什么？我输入python解释器的这些是为了向你展示一些小把戏。你还没有基础过`class` ，我们接下来将会学习它。至今为止，你看到python 输出`test() takes exactly 1 argument (2 given)`。如果你看到了意味着python 将`a.test("hello")` 换成了
`test(a, "hello")`，然后在某个地方某些人搞混了，并且没有为a添加参数

这里可能有很多要掌握的东西，但我们只打算用少量练习来强化你对这一概念的理解。让我们正式开始，这里有一个混合了`string`和`list`的有趣的练习。

```py
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split('')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding:", next_one
    stuff.append(next_one)
    print "There are %d items now." % len(stuff)

print "There we go :", stuff

print "Let's do some things with stuff."


print stuff[1]
print stuff[-1]
print stuff.pop()
print ''.join(stuff)
print '#'.join(stuff[3:5])
```

**和列表相关的函数**<br>

要分割的字符串.split('分隔符'，分割次数) <br>
**作用：**通过指定分隔符对字符串进行切片

pop(要移除的列表元素对象)<br>
**作用：**移除列表中的一个元素，默认最后一个元素。并返回该元素的值

指定字符串.join(要连接的元素序列)<br>
**作用：**方法用于将序列中的元素以指定的字符连接生成一个新的字符串。


## 列表可以做什么
让我们聊聊你想做的那个类似《去钓鱼》的游戏吧。如果你不知道《去钓鱼》是什么，花一点时间去玩一下。为了做这个，你需要使用一些方法将牌的概念用python实现。这时你需要用到一个东西：数据结构。

什么是数据结构？数据结构就是数据组织的方式。理解它不难，尽管有些数据结构异常复杂。但它们所做的无非是在程序中以合理的方式存储数据，这样，你能通过不同的方式去访问数据。

列表就是一种常见的数据结构。你可以通过标签去存储或访问列表中的数据。列表在现实世界中是什么呢？我们还用套牌来举例：

1. 你有一堆有值的牌
2. 这些牌在一个牌堆，表，或者一个从首牌到末牌的表
3. 你可以从顶部抽牌，或从底部抽或从中间随机抽
4. 如果你想找其中一张特殊的牌，你需要获取整副牌然后找到这张牌

从我的描述中你可以了解到列表的一些内容：

**一个有序的列表**<br>
是的，一副牌就是从第一张牌到最后一张牌的有序集合|

**你想要存储的东西**<br>
是的，牌就是我想要存储的东西|

**随机访问**<br>
是的，我能从这副牌里任意抓取一张牌|

**线性访问**<br>
是的，如果我想找到一张特殊的牌，我可以从首牌开始，一张张往后查找|

**通过标签访问**<br>
大多数情况下，你要访问比如第19个列表元素，你得一个个查过去。python允许你使用标签直接访问到目标元素。

## 什么时候去用列表

当你遇到和列表数据结构匹配的东西时，你可以使用列表去表示它。
1. 如果你需要排序，记住，这是列表顺序，不是排序的顺序。列表不会为你排序
2. 如果你需要使用`list[num]`去访问内容，记住使用时num从0开始
3. 如果你需要从第一个元素访问到最后一个。记住使用`for-loop`

## 练习

1. 将每一个函数的调用过程搞清楚，看看python是怎么处理他们的。比如more_stuff.pop() is pop(more_stuff)
2. 解释两种不同的调用方法。For example, more_stuff.pop() 这么解释，在more_stuff上调用pop函数。pop(more_stuff)则是调用pop函数，使用mystuff参数。他们其实是一回事
3. 去看一些面向对象编程的东西。困惑的话也别担心，慢慢来。
4. 看看python中的class是什么，不要看其他语言中的class。那只会令你误入歧途
5. 如果你不懂我讲了什么也别担心。如果你觉得面向对象编程很难，你可以尝试使用函数程序设计
6. 在现实世界中找到10个适合列表数据结构的东西，试着写一些使用它们的脚本