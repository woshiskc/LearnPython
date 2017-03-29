# 那是什么 #

----------
在练习9中我放出了一些新东西，要注意了。我使用了2种方法去显示多行字符串。第一种方法：我将`\n`放在月份名字(文本)之间。这样从这个符号往后的文本就显示在了不同的行。

这个`\`反斜杠加字符构成转义序列，它将很难打出来的许多字符编码为1个字符串。接下来你可能要用到有不同字符的转义序列。我们将尝试一些转义序列，这样你就能明白他们是做什么的了

一个很重要的转义序列是忽略`'`或者`"`。想象一下你要将双引号加入到字符串中，如果你写成`"I "understand" joe."`python就会懵逼了。因为它会将`"understand"`识别为一个字符串。你需要告诉python`"`这个是字符串的一部分，不是真的双引号

为了解决这个问题，你忽略掉双引号和单引号，这样python就知道把他们是字符串了。举例说明：


>"I am 6'2\" tall."  # escape double-quote inside string<BR>
>'I am 6\'2" tall.'  # escape single-quote inside string

第二种方式你可以用三引号`"""`。你仍然可以将许多行文本在两个`"""`之间。我们将尝试这种方式

>tabby_cat = "\tI'm tabbed in."<br>
persian_cat = "I'm split\non a line."<br>
backslash_cat = "I'm \\ a \\ cat."

>fat_cat = """<br>
I'll do a list:<br>
\t* Cat food<br>
\t* Fishies<br>
\t* Catnip\n\t* Grass<br>
"""

>print tabby_cat<br>
print persian_cat<br>
print backslash_cat<br>
print fat_cat

**转义序列**

|Escape|	What it does.<br>|
|---|---|
|`\\`|    Backslash (\)<br>|
|`\'`|	Single-quote (')<br>|
|`\"`|	Double-quote (")<br>|
|`\a`|   ASCII bell (BEL)<br>|
|`\b`|	ASCII backspace (BS)<br>|
|`\f`|	ASCII formfeed (FF)<br>|
|`\n`|	ASCII linefeed (LF)<br>|
|`\N{name}`|	Character named name in the Unicode database (Unicode only)<br>|
|`\r`|	Carriage Return (CR)<br>|
|`\t`|	Horizontal Tab (TAB)<br>|
|`\uxxxx`|	Character with 16-bit hex value xxxx (u'' string only)<br>|
|`\Uxxxxxxxx`|	Character with 32-bit hex value xxxxxxxx (u'' string only)<br>|
|`\v`|	ASCII vertical tab (VT)<br>|
|`\ooo`|	Character with octal value ooo|

## 练习 ##
- 记下所有转义序列
- 用`'''`三单引号代替。你能明白为什么你可以用这个代替`"""`么？
- 结合使用转义序列和格式化字符串，去创造一些复杂的格式
- 还记得`%r`么，将`%r`和双引号单引号转忽略字符一起使用，把他们打印出来。对比`%r`和`%s`。
