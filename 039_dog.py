# 第9章 类

# 9.1 创建和使用类 page 138


class Dog():  # 在Python中,首字母大写的名称指的是类。
    """一次模拟小狗的简单尝试"""

    # __init__()是一个特殊的方法,每当你根据Dog类创建新实例时,Python都会自动运行它。
    # 在这个方法的名称中,开头和末尾各有两个下划线,这是一种约定,旨在避免Python默认方法
    # 与普通方法发生名称冲突。
    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):  # 类中的函数称为方法
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")

"""
我们将方法__init__()定义成了包含三个形参: self、 name和age。在这个方法的定义中,形
参self必不可少,还必须位于其他形参的前面。为何必须在方法定义中包含形参self呢?因为
Python调用这个__init__()方法来创建Dog实例时,将自动传入实参self。每个与类相关联的方法
调用都自动传递实参self,它是一个指向实例本身的引用,让实例能够访问类中的属性和方法。
我们创建Dog 实例时,Python将调用Dog类的方法__init__()。我们将通过实参向Dog()传递名字和
年龄; self会自动传递,因此我们不需要传递它。每当我们根据Dog类创建实例时,都只需给最
后两个形参(name和age)提供值。
"""
