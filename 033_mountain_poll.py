# 7.3.3 使用用户输入来填充字典 page 112

responses = {}

# 设置一个标志,指出调查是否继续
polling_active = True

while polling_active:

    # 提示输入被调查者的名字和回答
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # 将答卷存储在字典中
    responses[name] = response

    # 看看是否还有人要参与调查
    repeat = input("Would you like to let another person respond? (yes/ no) ")

    if repeat == 'no':
        polling_active = False

# 调查结束,显示结果
print("\n--- Poll Results ---")

for name, response in responses.items():
    print(name + " would like to climb " + response + ".")

# 第8章 函数 page 114

# 函数是带名字的代码块,用于完成具体的工作。

print('---' * 80)


def greet_user():
    """显示简单的问候语"""
    print("Hello!")


greet_user()

'''
函数下面的注释是被称为文档字符串(docstring)的注释,描述了函数是做什么的。
文档字符串用三引号括起,Python使用它们来生成有关程序中函数的文档。
'''

# 8.1.1 向函数传递信息 page 115


def greet_user(username):
    """显示简单的问候语"""
    print("Hello, " + username.title() + "!")


greet_user('jesse')

# 8.1.2 实参和形参

# 8.2 传递实参

# 8.2.1 位置实参 page 116


def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet('hamster', 'harry')


# 1. 调用函数多次


def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

# 2. 位置实参的顺序很重要

# 8.2.2 关键字实参 page 118


def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet(animal_type='hamster', pet_name='harry')

# 关键字实参的顺序无关紧要,因为Python知道各个值该存储到哪个形参中。

describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

# 8.2.3 默认值 page 118

# 给形参指定默认值后,可在函数调用中省略相应的实参。使用默认值可简化函数调用,
# 还可清楚地指出函数的典型用法。


def describe_pet(pet_name, animal_type='dog'):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet(pet_name='willie')
describe_pet('willie')

'''
请注意,在这个函数的定义中,修改了形参的排列顺序。由于给animal_type指定了默认值,
无需通过实参来指定动物类型,因此在函数调用中只包含一个实参——宠物的名字。然而, Python
依然将这个实参视为位置实参,因此如果函数调用中只包含宠物的名字,这个实参将关联到函数
定义中的第一个形参。这就是需要将pet_name放在形参列表开头的原因所在。
'''

# 如果要描述的动物不是小狗,可使用类似于下面的函数调用:
describe_pet(pet_name='harry', animal_type='hamster')

'''
注意使用默认值时,在形参列表中必须先列出没有默认值的形参,再列出有默认值的实参。
这让Python依然能够正确地解读位置实参。
'''

# 8.2.4 等效的函数调用 page 119

# 一条名为Willie的小狗
describe_pet('willie')
describe_pet(pet_name='willie')

# 一只名为Harry的仓鼠
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')

# 8.2.5 避免实参错误 page 120









