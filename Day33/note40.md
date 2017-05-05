# 40 模块，类，对象
--------------------------
python是“一种面向对象的编程语言”。这意味着python中有类的概念。类是一种独有的构建软件的方式。通过使用类，你可以使你的程序变得条理清晰，可读性更强。

## 模块就像字典
你已经知道字典是怎么被创建和使用的，同时字典也是一种映射的方式。如果你有一个含有 apple 键的字典，然后你想获取它，你可以这么做：

```py
mystuff = {'apple':"I AM APPLES!"}
print mystuff['apple']
```

顺着这个思路，思考一下什么是模块：
1. 一个含有许多函数和变量的python文件
2. 你导入了这个文件
3. 你可以使用.操作符访问这个模块中的函数和变量

想象一下我有一个模块。我决定把它命名为mystuff.py。然后我在这个文件中放了一个叫apple的函数。mystuff.py就是一个模块：
```py
# this goes in mystuff.py
def apple()：
    print "I AM APPLES!"
```

一旦我有了这段代码，我就能将mystuff模块导入进来，并且访问模块中的apple函数：
```py
import mystuff
mystuff.apple()
```

我也能够在mystuff模块中加入一个名为tangerine的变量：
```py
def apple()：
    print "I AM APPLES!"

# this is just a variable
tangerine = "Living reflection of a dream. Hi, NEO"
```

我能够用同样的方式访问到这个变量：
```py
import mystuff

mystuff.apple()
print mystuff.tangerine
```

回想一下字典，可以看到模块十分类似字典，只是在语法上不同，让我们对比一下：
```py
mystuff['apple'] # 从字典中获取apple元素
mystuff.apple() # 从模块中调用apple函数
mystuff.tangerine # 从模块中访问tangerine变量
```

由此，我们了解到python中一个十分常见的模式：
1. 获得一个键值对应的容器。比如import sth
2. 使用键名称访问这个容器中的元素。比如 sth.sth_else

在字典中，这个键是字符串，格式为[key]。在模块中，这个键是标识符，叫id也行。格式是.key

## 类就像模块
饶了一圈儿终于讲到类了。类是什么？类中可以放置许多函数和数据，相当于一个容器。你可以可使用.操作符去访问它们。
如果我要创建一个类似于mystuff模块的类，我会这么写：
```py
class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"
    
    def apple(self):
        print "I AM APPLES!"
```

这TM看起来比模块复杂多了，你应该能理解其中apple函数的定义。但会对__init__()函数 和 使用self.tangerine将tangerine实例化 感到困惑。

这就是为什么要用类替代模块的原因。类可以实例化出成千上万的对象，彼此互不干扰。但是模块不行。在你理解这个之前，你需要先搞明白对象和类的关系。

## 对象就像导入（引用）
如果说类像一个迷你的模块，那么对于类来说，应该有一个类似的方法去导入或引用。这个方法叫“实例化”，这是一种对“创建”很富于想象，但又令人讨厌，有点小聪明的叫法。类被实例化后就称作对象。

实例化类的方式：
```py
thing = MyStuff()
thing.apple()
print thing.tangerine
```

1. python找到MyStuff()，然后发现它是你定义的一个类
2. python为所有在类中定义的函数生成一个空对象
3. python会看你是否创建了__init__函数，如果你创建了，它就会调用这个函数初始化你新创建的空对象。
4. 在mystuff的__init__函数中我得到了一个额外的变量self，self是一个python为我创建的空对象。我能够设置一些变量在上面
5. 在这里我将成员变量self.tangerine设置为一段歌词，然后我初始化这个对象
6. 现在，python能够将这个新生成的对象赋给一个变量，然后我就可以使用它了

这是关于python如何使用类和对象的基础方法。这里并没有给你一个类，而是教你使用类的方法。
综上：
1. 类就像蓝图或定义，可以生成新的模块
2. 实例化就是生成并同时导入新模块。实例化也意味着，从类中创建一个新对象。
3. 你创建的新模块就是一个对象，把对象赋给一个变量，然后你就可以使用它了

## 从一个事物中获取另一个事物

现在我有三种访问方法：
```py
# dict style
mystuff['apples']

# module style
mystuff.apples()
print mystuff.tangerine

# class style
thing = MyStuff()
thing.apples()
print thing.tangerine
```

关于三种键值对应容器你可能有一堆疑问，先记着这些疑问。敲出下面代码，让它们运行起来。下一课我将解答你这些疑问。
```py
class Song(object):
    def __init__(self,lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line


happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])


happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
```

## 练习
1. 写更多的歌，用这种形式，确保你理解了你传了一个字符串列表作为歌词
2. 将歌词放入一个单独的变量，然后把该变量传入类并使用它
3. 看看你能不能修改这个类让它做更多的事情
4. 上网查面向对象编程，尝试理解