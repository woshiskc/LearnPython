# 24 更多练习
-------------------------
你已经到达这个章节的末尾。现在你应该掌握了足够多的知识去学习怎么样去写程序。在此之前你应该再做一些练习。这些练习很长，有助于建立耐心。下面的练习也像这样。坚持做下去，记得检查。

```
print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "--------------"
print poem
print "--------------"


five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates         # 函数返回多个值的情况


start_point = 10000
beans, jars, crates = secret_formula(start_point)  # 将函数返回值，依次分别赋给三个变量

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)
```

## 练习

1. 确保你已经做了检查。从后向前重读，大声读出来，为每一个不容易理解的地方写注释
2. 有目的的改变程序，运行它，观察出现的错误。确保你可以修复这些错误。

## 其他

- 给一个变量赋值时，赋值对象可以是一个有返回值的函数，可以是数字也可以是字符串，也可以是一个表达式

- 可以给多个变量同时赋值。例如:
```
var1,var2,var3 = 1, 2 ,3
```