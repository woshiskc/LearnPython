# 函数和文件
----------------------
记得使用函数检查表。然后做这个练习。注意函数和文件是怎样协同工作的。

>from sys import argv
>
>script, input_file = argv
>
>def print_all(f):<BR>
>    print f.read()
>
>def rewind(f):<BR>
>    f.seek(0)
>
>def print_a_line(line_count, f):<BR>
>    print line_count, f.readline()
>
>current_file = open(input_file)
>
>print "First let's print the whole file:\n"
>
>print_all(current_file)
>
>print "Now let's rewind, kind of like a tape."
>
>rewind(current_file)
>
>print "Let's print three lines:"
>
>current_line = 1<BR>
>print_a_line(current_line, current_file)
>
>current_line = current_line + 1<BR>
>print_a_line(current_line, current_file)
>
>current_line = current_line + 1<BR>
>print_a_line(current_line, current_file)

## 练习

1. 为每一行写注释
2. 每次`print_a_line`运行的时候，你将`current_line`变量传入进去。写出`current_line`在每个函数中代表什么。并且追踪它，看他是怎么在`print_a_line`中变为`line_count`
3. 查看每一个用到函数的地方，检查函数定义，确认你给了正确的参数
4. 上网查询，`seek`函数是怎么操作文件的。尝试使用`pydoc file`，看你能弄明白它不能，然后尝试`pydoc file.seek`查看`seek`功能。
5. 研究`+=`符号用法。试着用上`+=`符号重写脚本

## 其他

**seek函数**

seek() 方法用于移动文件读取指针到指定位置。

seek(偏移量,偏移量参数)

偏移量代表需要移动偏移的字节数。

偏移量参数默认值为0，代表从文件开头算起；为1，代表从当前位置算起；2代表从文件末尾算起

**形参**

形式参数不参与函数功能。

**+=**

'x += y'相当于'x = x + y'

将x+y的值赋值给x
