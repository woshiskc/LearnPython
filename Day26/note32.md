# 32 表和循环
------------------------
现在你应该体验过一些很有意思的程序了。如果你继续下去，你会发现你能将学过的东西用if条件格式和布尔表达式串联在一起，让程序更加智能

然而，程序也需要快速做一些重复的事情。接下来的练习中，我们将用`for-loop`循环，创建和打印不同的列表。当你做这个练习的时候，你将体会到他们运作的机制是什么

在你使用`for-loop`之前，你需要一个方法去存储循环的结果。最好的方式是用`list`。`list`顾名思义，可以理解为他是一个装东西的容器。python中列表通常这么定义：

```
hairs = ['brown','blond','red']
eyes = ['brown','blue','green']
weights = [1, 2, 3, 4]
```
从上面你可以看到，列表由[开始，然后是列表中的各个元素，由,分隔。最后以]结束。在python中，可以将一个列表赋给一个变量。

然后我们使用`for`循环，创建列表并打印：

```
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print "This is count %d" % number

# same as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print "I got %r" % i

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print "Adding %d to the list." % i
    # append is a function that lists understand
    elements.append(i)

# now we can print them out too
for i in elements:
    print "Element was: %d" % i
```

## 练习

1. 学习`range`用法，查询`range`函数并掌握它
2. 你能够完全不用`for-loop`，然后将22行中`range(0,6)`直接赋给`element`吗？
3. 查阅python文档，看看你能不能对列表进行`append`之外的其他操作。




## 列表元素

可以是字符串，数字，列表


## for-loop格式

for 参数 in 参数取值区间

循环次数取决于区间中参数的数量。循环体中可以嵌套条件判断，根据情况终止循环。

## 列表函数

**append函数**

a.append(b)
将b作为一个列表元素，加入到列表a末尾

**extend函数**

a.extend(b)
将b中多个元素追加到a列表中，相当于扩充了a列表


