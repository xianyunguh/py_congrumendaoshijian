# 5.3.3 if-elif-else 结构 page 72

age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")

# 上例改进

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print("Your admission cost is $" + str(price) + ".")

# 5.3.4 使用多个 elif 代码块 page 73

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5

print("Your admission cost is $" + str(price) + ".")

# 5.3.5 省略 else 代码块 page 74

# Python并不要求if-elif结构后面必须有else代码块。

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5

print("Your admission cost is $" + str(price) + ".")

# 5.3.6 测试多个条件 page 74

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")


# 5.4 使用 if 语句处理列表 page 76

# 5.4.1 检查特殊元素

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")

#

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")

# 5.4.2 确定列表不是空的 page 78

print('*'*80)
requested_toppings = []

if requested_toppings:  # 如果列表为空，则返回False
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
        print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

# 5.4.3 使用多个列表 page 78

available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
    print("\nFinished making your pizza!")

# 5.5 设置 if 语句的格式 page 80

'''
在条件测试的格式设置方面, PEP 8提供的唯一建议是,在诸如 ==、>=和<= 
等比较运算符两边各添加一个空格,例如,if age < 4:要比 if age<4: 好。

'''






