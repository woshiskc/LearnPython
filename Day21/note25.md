# 25 更多更多练习
--------------------------
我们将会做更多涉及函数和变量的练习，以保证你能更深刻的理解它们。
这个练习有点不一样。你不用直接运行它，你将在python中引用它，然后调用其中的函数。

```
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
```

## 练习

- import脚本`ex25`后。使用`help(ex25)`可以查看脚本中所有函数及函数下的文档说明。使用`help(ex25.break_words)`则查看`ex25`中`break_words`函数及文档说明。需要注意的是，使用`help()`并不能查看函数内容。

- 在函数中，两个`"""`符号间的文本内容，叫文档说明或文档注释。

- 每次引用函数都打`ex.`很麻烦，可以在导入脚本的时候，输入`from ex25 import *`，这相当于把`ex25`中所有的东西都导入进来。


- **几个新函数**

**split()函数**<br>
    格式 `split("str",num)`<br>
    `split`通过指定分隔符，对字符串进行分隔。<br>
    **`str`**:指定分隔符，默认为所有空字符，包括空格、换行`\n`、制表符`\t`等<br>
    **`num`**:分隔次数<br>
    函数返回值为分隔后的字符串列表。

**sorted()函数**<br>
    格式 `sorted(...)`<br>
    `sorted`可对容器内数据进行排序。与`sort`函数不同的是，`sorted`会生成一个排好序的新容器。`sort`只在原容器中排序。<br>
    ```
    sorted(iterable, cmp=None, key=None, reverse=False) --> new sorted list
    ```<br>
    **`iterable`**：待排序的可迭代类型的容器;<br>
    **`cmp`**：用于比较的函数，比较什么由`key`决定,有默认值，迭代集合中的一项;<br>
    **`key`**：用列表元素的某个已命名的属性或函数（只有一个参数并且返回一个用于排序的值）作为关键字，有默认值，迭代集合中的一项;<br>
    **`reverse`**：排序规则. `reverse = True`（正序） 或者 `reverse = False`（倒序），有默认值。<br>
    返回值：是一个经过排序的可迭代类型，与`iterable`一样。

**pop()函数**<br>
    格式`pop(obj)`<br>
    `pop`函数可以移出列表中的一个元素。默认为最后一个元素。并且返回该元素值。<br>
   **`obj`**:表要移出列表元素的对象。