# 33 While 循环
-----------------------
现在介绍一种新循环，while-loop。当判断条件为True时，一个while-loop下的代码块会持续循环运行。

while循环和for循环不一样的是，当while循环执行一次后，会回到while代码块的开头，当while循环条件表达式为真时，while循环中的代码会再运行一遍。然后重复这个过程。直到表达式结果为False

while循环会有一个问题。有些时候他会一直运行，停不下来。如果你希望这个程序跑到天荒地老，那么这种情况真的很不赖。但事实上，多数情况下你需要这个循环能停下来。

为了解决这个问题，有许多规则需要注意：
1. 谨慎使用while-loop，最好多用for-loop
2. 检查你的while条件判断语句，确保结果会变为Fasle
3. 为了解决疑惑，将测试变量在while-loop下打印出来，看看到底发生了什么

```
i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)

    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i


print "The numbers: "

for num in numbers:
    print num

```
## 练习

1. 将while-loop转换成一个你可以调用的函数，在( i < 6 )中，使用一个变量代替6
2. 使用这个函数重写这个脚本。尝试不同的数字
3. 加入一个变量，作为该函数参数，该参数为x，i = i + x。改变i递增量
4. 使用for-loop和range重写脚本。你还会需要增量器吗？如果你不去掉他会发生什么？

