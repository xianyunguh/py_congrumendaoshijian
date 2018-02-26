# 8.6 将函数存储在模块中 page 133

# 8.6.1 导入整个模块

"""代码行import pizza让Python打开文件pizza.py,并将其中的所有函
数都复制到这个程序中。你看不到复制的代码,因为这个程序运行时,Python在幕后复制这些代
码。
"""

import hanshu_pizza

hanshu_pizza.make_pizza(16, 'pepperoni')
hanshu_pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 8.6.2 导入特定的函数 page 134

"""导入模块中的特定函数,语法如下:
from module_name import function_name
通过用逗号分隔函数名,可根据需要从模块中导入任意数量的函数:
from module_name import function_0, function_1, function_2

若使用这种语法,调用函数时就无需使用句点。
"""

from hanshu_pizza import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 8.6.3 使用 as 给函数指定别名 page 134

"""如果要导入的函数的名称可能与程序中现有的名称冲突,或者函数的名称太长,可指定简短
而独一无二的别名——函数的另一个名称,类似于外号。要给函数指定这种特殊外号,需要在导
入它时这样做。
下面给函数make_pizza()指定了别名mp()。这是在import语句中使用make_pizza as mp实现的,
关键字as将函数重命名为你提供的别名:
"""

from hanshu_pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')


# 8.6.4 使用 as 给模块指定别名 page 135

import hanshu_pizza as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 8.6.5 导入模块中的所有函数

from hanshu_pizza import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 8.7 函数编写指南 page 136

"""
编写函数时,需要牢记几个细节。
1.给函数指定描述性名称,且只使用小写字母和下划线。

2.每个函数都应包含简要地阐述其功能的注释,该注释应紧跟在函数定义后面,并采用文档字
符串格式。

3.给形参指定默认值时,等号两边不要有空格:
def function_name(parameter_0, parameter_1='default value ')
对于函数调用中的关键字实参,也应遵循这种约定:
function_name(value_0, parameter_1='value')

4.如果形参很多,导致函数定义的长度超过了79字符,可在函数定义中输入左括号后按回车键,
并在下一行按两次Tab键,从而将形参列表和只缩进一层的函数体区分开来。

def function_name(
        parameter_0, parameter_1, parameter_2 ,
        parameter_3, parameter_4, parameter_5 ):
    function body...

5.如果程序或模块包含多个函数,可使用两个空行将相邻的函数分开,这样将更容易知道前一
个函数在什么地方结束,下一个函数从什么地方开始。

所有的import语句都应放在文件开头,唯一例外的情形是,在文件开头使用了注释来描述整
个程序。

"""