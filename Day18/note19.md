# 练习19：函数和变量
-------------------

函数中可能有很多让你困惑的地方。不要担心。继续练习，按照上一节中你订立的检查表中的内容去做，一步步来，你终将掌握函数。

这里有一个需要我们强调的内容，你可能还没有意识到。函数中的变量和脚本中的变量没有关联。下面的练习能让我们看到这一点。

>def cheese_and_crackers(cheese_count,boxes_of_crackers):<br>
>    print "You have %d cheeses!"% cheese_count<br>
>    print "You have %d boxes of crackers!"% boxes_of_crackers<br>
>    print "Man that's enough for a party!"<br>
>    print "Get a blanket.\n"
>
>print "We can just give the function numbers directly:"<br>
>cheese_and_crackers(20, 30)
>
>print "OR, we can use variables from our script:"<br>
>amount_of_cheese = 10<br>
>amount_of_crackers = 50
>
>cheese_and_crackers(amount_of_cheese, amount_of_crackers)
>
>print "We can even do math inside too:"<br>
>cheese_and_crackers(10 + 20, 5 + 6)
>
>print "And we can combine the two, variables and math:"<br>
>cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


 上面列出了我们给函数`cheese_and_crackers`传递不同参数后，函数的输出情况。我们能直接传数字、变量、数学表达式甚至是包含变量的数学表达式
 
 事实上你可以使用 `=` 去命名一些事物。你可以将这些变量当做参数传递给函数。

## 练习

 1. 为上面代码写注释
 2. 从后向前读代码，说出每一个重要的字符
 3. 写一个你自己设计的函数。尝试以10种方式运行。   