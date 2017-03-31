# 提示用户
当你输入`raw_input()`时你输入了 `(` 和 `)` 字符，括号字符。这类似你为了使用某种格式而使用特殊的变量，比如`"%s %s" % (x, y)`.对于 `raw_input` 你可以为用户写提示，好让他们知道需要输入什么。将你想让用户看到的字符串写入` () `中，像这样：

>y = raw_input("Name? ")

它给用户的提示是`"Name？"`,然后将结果存入变量 `y `。这种方式就类似你问别人一个问题然后得到答案。

这意味这我们可以重写上一个练习，仅使用 `raw_input` 去完成所有提示

>age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")
>
>print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)

## 练习
1. 在命令提示行中，我们通常让`python`去跑你写的脚本。输入 `pydoc raw_input` 看看会显示什么。如果你用`windows`，输入 `python -m pydoc raw_input`

2. 输入`q` 退出`pydoc`

3. 上网查`pydoc`命令的作用

4. 使用`pydoc`阅读关于`open`，`file`，`os`和`sys`相关的内容。看不懂没关系，读然后记下你感兴趣的东西

## 问答
**为啥当我运行`pydoc` 的时候出现了`SyntaxError: invalid syntax `错误？**

答：你没有在命令提示行下运行`pydoc`。你可能在`python`下运行了。先退出`python`再运行

**为什么我的`pydoc`不像你的那样有停顿和空间？**

答：有些时候，如果帮助文档短到足以在一屏内显示，`pydoc`就会那么做

**当我运行`pydoc`时，得到内部不识别的内容？**

答：某些版本的`Windows`不包含这些命令，导致`pydoc`出问题。你可以上网去查`python`相关的信息，如果你需要的话

**为什么我这么写不行：`print "How old are you?" , raw_input()`？**

答：`pyhton`认为这是非法的。


