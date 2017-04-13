# 27 学习逻辑
-------------------
在python中，有一些字符或短语，用来决定某个事物在逻辑上是真还是假。

|逻辑运算符| 说明|
|------|-------|
|and| 且|
|or| 或|
|not| 非|
|!=| 不等于|
|==| 等于|
|>=| 大于等于|
|<=| 小于等于|
|True| 真|
|False| 假|

## 真值表

**NOT 非**

非假即真，非真即假

|NOT|True?|
|-------|-----|
|not False|	True|
|not True|	False|

**OR 或**

有真即真

|OR	|True?|
|------|------|
|True or False|True|
|True or True|True|
|False or True|True|
|False or False|False|


**AND 且**

有假即假

|AND	|True?|
|------|------|
|True and False|	False|
|True and True|	True|
|False and True|	False|
|False and False|	False|

**NOT OR**

真值与OR相反

|NOT OR|	True?|
|------|------|
|not (True or False)|	False|
|not (True or True)|	False|
|not (False or True)|	False|
|not (False or False)|	True|

**NOT AND**

真值与AND相反

|NOT AND|	True?|
|------|------|
|not (True and False)|	True|
|not (True and True)|	False|
|not (False and True)|	True|
|not (False and False)|	True|

**!= 不等**

两边存在不等关系为真

|!=|	True?|
|------|------|
|1 != 0|	True|
|1 != 1|	False|
|0 != 1|	True|
|0 != 0|	False|

**== 等于**

两边存在相等关系为真

|==|	True?|
|------|------|
|1 == 0|	False|
|1 == 1|	True|
|0 == 1|	False|
|0 == 0|	True|
