# 第5章 if语句 page 64

# 5.1 一个简单示例 page 64

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# 5.2 条件测试 page 65

# 5.2.1 检查是否相等

 '''
 一个等号是陈述;car = 'audi',可解读为“将变量car的值设置为 'audi'”。
 两个等号是发问;car == 'audi'可解读为“变量 car的值是'bmw'吗?”。

 '''

# 5.2.2 检查是否相等时不考虑大小写 page 65

# 在Python中检查是否相等时,是区分大小写的。

car.lower() == 'audi' # 函数lower()不会改变car的值。



