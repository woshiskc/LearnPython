# 提示和传递参数
------
让我们做一个一起使用`argv`和`raw_input`练习，然后向用户问一些特定的问题。在下一个练习（读写文件）中你将会用到这些。这个练习中，我们将使用`raw_input`打印一个简单的带>的提示。这有点类似文字冒险游戏。

>from sys import argv
>
>script, user_name = argv<BR>
prompt = '> '<BR>
>
>print "Hi %s, I'm the %s script." % (user_name, script)<BR>
print "I'd like to ask you a few questions."<BR>
print "Do you like me %s?" % user_name<BR>
likes = raw_input(prompt)
>
>print "Where do you live %s?" % user_name<BR>
lives = raw_input(prompt)<BR>
>
>print "What kind of computer do you have?"<BR>
computer = raw_input(prompt)<BR>
>
>print """<BR>
Alright, so you said %r about liking me.<BR>
You live in %r.  Not sure where that is.<BR>
And you have a %r computer.  Nice.<BR>
""" % (likes, lives, computer)

我们定义了变量`prompt`去存储我们想要的提示。然后我们将其给予`raw_input`这样就不用一遍遍输入。现在我们如果想要增加一些其他的提示，我们仅需改变这个变量，然后重新运行脚本。十分便利

## 练习
1. 理解Zork和冒险游戏到底是啥。试着找出一个版本，然后玩一下。
2. 将`prompt`变量用其他变量彻底替换。
3. 在你的脚本中使用其他参数，类似在上个练习中做的那样`first, second = ARGV`
4. 确保你理解了在最后一行打印输出的内容里，我是怎么将`"""`和`%`格式融合使用的