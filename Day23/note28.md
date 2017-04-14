# 28 布尔练习
----------------
昨天的练习中涉及的逻辑组合，通常被叫做布尔逻辑表达式。布尔运算出现在程序的各个角落。是最为常见的运算。

在这个练习中，你将做一些逻辑练习，并且尝试在python中运行。看下面所有表达式，思考他们的结果（真，假）。并把答案记下来，然后用python运行，验证答案是否正确。

1. True and True  **TRUE**
2. False and True  **FALSE**
3. 1 == 1 and 2 == 1  **FALSE**
4. "test" == "test"  **TRUE**
5. 1 == 1 or 2 != 1  **TRUE**
6. True and 1 == 1   **TRUE**
7. False and 0 != 0   **FALSE**
8. True or 1 == 1  **TRUE**
9. "test" == "testing"  **FALSE**
10. 1 != 0 and 2 == 1  **FALSE**
11. "test" != "testing"  **TRUE**
12. "test" == 1   **FALSE**
13. not (True and False)  **TRUE**
14. not (1 == 1 and 0 != 1)  **FALSE**
15. not (10 == 1 or 1000 == 1000)  **FALSE**
16. not (1 != 10 or 3 == 4)   **FALSE**
17. not ("testing" == "testing" and "Zed" == "Cool Guy")  **TRUE**
18. 1 == 1 and (not ("testing" == 1 or 1 == 0))  **TRUE**
19. "chunky" == "bacon" and (not (3 == 4 or 3 == 3))  **FALSE**
20. 3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))  **FALSE**

你能够通过以下流程来解决逻辑判断问题：
1. 找到 `==` 或者 `!=` ，然后用他们的真值替换他们。
2. 找到每一个在括号中的 `and/or` 然后优先处理他们。
3. 找到每一个 `not`然后反转他
4. 找到余下的 `and/or` 然后处理他们
5. 当你经历了上面的步骤，你应该可以获得结果了

## 练习
----------------
1. 在python中，有很多类似`!= `和`==`的逻辑运算符。尽可能找到这些运算符。例如`<` or `<=`

2. 写出这些等运算符的名字，例如 `!=` 为 不等于

3. 将布尔逻辑表达式输入python ，验证输出结果


运行python。将逻辑表达式输入，按回车即可看到运算结果。
