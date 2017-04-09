# 函数的返回
-------------
你已经知道怎么用 `=` 符号去命名一个变量，并给付值给它（数字或字符串）。现在我们将向你展示怎么用 `=` 号和一个新的python关键字 `return` 从函数中返回变量的值。

    def add(a, b):
        print "ADDING %d + %d" % (a, b)
        return a + b

    def subtract(a, b):
        print "SUBTRACTING %d - %d" % (a, b)
        return a - b

    def multiply(a, b):
        print "MULTIPLYING %d * %d" % (a, b)
        return a * b

    def divide(a, b):
        print "DIVIDING %d / %d" % (a, b)
        return a / b


    print "Let's do some math with just functions!"

    age = add(30, 5)
    height = subtract(78, 4)
    weight = multiply(90, 2)
    iq = divide(100, 2)

    print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


    # A puzzle for the extra credit, type it in anyway.
    print "Here is a puzzle."

    what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

    print "That becomes: ", what, "Can you do it by hand?"

我们现在开始进行数学计算（加减乘除）。最后一行非常重要。在这一行我们输入了`return a+b `（在add函数中）。这段代码的作用如下：

1. 我们的函数有两个参数`a`和`b`。
2. 我们指出了我们的函数是做什么的。在这里是“加”
3. 然后我们告诉`python`这么做：我们返回加法`a+b`结果。你可以这么理解,我让`a`加上`b`然后返回他们
4. `python`让这两数相加。当函数结束时，我们可以将`a+b`的结果赋给一个变量。

## 练习
----------------------
1. 如果你不是很清楚`return`是怎么工作的。试着写几个函数，让他们返回一些值。
2. 在脚本最后，是一个谜语，我用一个函数的返回值做为另外一个函数的参数。我在这里使用了嵌套，所以从另外一个角度来说我使用函数创造了一个公式。看起来很奇怪。但是你运行脚本后就能看到结果。你要做的是找出正常的公式。
3. 一旦你使用公式解决了难题。看看当你定义函数的这个部分发生了什么。有目的的改变它，得到另外的值
4. 反向操作。写一个简单公式。使用函数通过同样的方式计算它。