# 8.4.1 在函数中修改列表 page 126


def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计,直到没有未打印的设计为止
    打印每个设计后,都将其移到列表completed_models中
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        # 模拟根据设计制作3D打印模型的过程
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")

    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# 理念,即每个函数都应只负责一项具体的工作。

# 8.4.2 禁止函数修改列表 page 129

# 要将列表的副本传递给函数,可以这样做: function_name(list_name[:])

print_models(unprinted_designs[:], completed_models)

# 8.5 传递任意数量的实参 page 130
print('---'*8)


def make_pizza(*toppings):
    """打印顾客点的所有配料
    形参名*toppings中的星号让Python创建一个名为toppings的空元组,并将收到的所有值都封
    装到这个元组中。
    """

    """概述要制作的比萨"""
    print("\nMaking a pizza with the following toppings:")

    for topping in toppings:
        print("- " + topping)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# 8.5.1 结合使用位置实参和任意数量实参 page 131

"""如果要让函数接受不同类型的实参,必须在函数定义中将接纳任意数量实参的形参放在最
后。Python先匹配位置实参和关键字实参,再将余下的实参都收集到最后一个形参中。
"""


def make_pizza(size, *toppings):
    """概述要制作的比萨"""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")

    for topping in toppings:
        print("- " + topping)


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')



