一、数据类型
    1、数字：支持基本算术运算和逻辑运算表达式

    2、字符串：支持格式化、支持[索引]格式匹配获取 以及字符串拼接，使用str.format()格式
    支持printf 使用% 运算符格式化字符串，支持切片

    3、列表：支持切片和索引，同样支持拼接 .append('元素') len(变量)
二、控制流程
    1、if 语句
    if 条件 ：
        表达式
           .
           .
           . 
        print
    elif 条件 :
        表达式
            .
            .
            .
        print
    else :
        表达式
        print    

    2、for 语句
    for 元素 in  集合：
        print 元素

    要以序列的索引来迭代，您可以将 range() 和 len() 组合如下:
    items() 争对于散列类型集合

    3、break 和 continue 语句，以及循环中的 else 子句
    break 语句，和 C 中的类似，用于跳出最近的 for 或 while 循环.
    
    4、pass 语句
    跳过什么也不做

三、定义函数
1、格式:
def 函数名（）：
    循环语句
    表达式
    输入输出表达式

2、调用函数
函数名（有参数则输入，无参则不输入）     

Lambda 表达式
可以用 lambda 关键字来创建一个小的匿名函数。这个函数返回两个参数的和： lambda a, b: a+b 。Lambda函数可以在需要函数对象的任何地方使用。它们在语法上限于单个表达式。从语义上来说，它们只是正常函数定义的语法糖。与嵌套函数定义一样，lambda函数可以引用所包含域的变量:

>>>
>>> def make_incrementor(n):
...     return lambda x: x + n
...
>>> f = make_incrementor(42)
>>> f(0)
42
>>> f(1)
43


下面是一个多行文档字符串的例子:

>>>
>>> def my_function():
...     """Do nothing, but document it.
...
...     No, really, it doesn't do anything.
...     """
...     pass
...
>>> print(my_function.__doc__)
Do nothing, but document it.


四、数据结构
1、列表
   格式： list = []
列表内置方法或内置函数、包含了对列表的元素的增删改查、列表的切片、迭代输出、反转、排序、统计、拷贝

2、列表作为栈的使用
规则：后进先出
stack = []
入栈：stack.append(元素)
出栈：stack.pop() 获得栈顶元素

3、列表作为队列使用
规则：先进先出
在列表尾部添加元素和弹出元素非常快 基于collection.deque
queue = deque(["eric","sda","sdfa"]) 
入队：queue.append("asdfa")
出队：queue.popleft()  #first out
eric

4、列表推导式

嵌套列表推导式
matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],[13,14,15,16]]
#矩阵转置一次，发生90度偏移
a= [[row[i] for row in matrix] for i in range(4)]    
print(a)
b= [[row[i] for row in a] for i in range(4)] 
print(b)


5、元组、序列类型 --- list, tuple, range

元组由几个被逗号隔开的值组成
 其中包含了不同的数据类型

v = ([1, 2, 3], [3, 2, 1])
 u = t, (1, 2, 3, 4, 5)

6、集合
集合支持set()

可进行交并补的推导式运算

7、字典
字典是python 常见的数据类型
结构：dict = [key : value, key, : value1, key2 : value2]

tel = {'jack': 4098, 'sape': 4139}
 通过数组下标定义的方式插入字典，是一种索引型数据类型
基础是一个有键和值组成 ，可以看作一个键值 list
 可以通过iteam 方式获得键和值
 key : value
 或则使用zip() 函数一一匹配

 五、错误异常

语法错误又称解析错误，可能是你在学习Python 时最容易遇到的错误:

即使语句或表达式在语法上是正确的，但在尝试执行时，它仍可能会引发错误。

处理异常：格式

在控制语句内
    try:
        表达式
        输出
        输入
    except error as err
        print(error,...)

finally 


六、类
定义各种内部的函数、python 正意义上的编程

类似Java编程有变量、参数、作用域、封装继承多态的特性

七、标准类库
操作系统级别接口
os 模块 每一个动作都类似于计算的操作
详细再看os模块内部函数定义

