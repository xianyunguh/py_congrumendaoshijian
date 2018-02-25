# 第6章 字典 page 81

# 6.1 一个简单的字典 page 81

alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

# 6.2 使用字典 page 82

# 6.2.1 访问字典中的值  page 82

alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

# 6.2.2 添加键—值对 page 83

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0  # 新增键值对
alien_0['y_position'] = 25
print(alien_0)

'''
注意,键—值对的排列顺序与添加顺序不同。 Python不关心键—值对的添加顺序,
而只关心键和值之间的关联关系。

'''

# 6.2.3 先创建一个空字典 page 83

alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

# 6.2.4 修改字典中的值 page 84

alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")


'''
来看一个更有趣的例子:
对一个能够以不同速度移动的外星人的位置进行跟踪。为此,我们
将存储该外星人的当前速度,并据此确定该外星人将向右移动多远:
'''

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))

# 向右移动外星人
# 据外星人当前速度决定将其移动多远

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:

    # 这个外星人的速度一定很快

    x_increment = 3

# 新位置等于老位置加上增量

alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))

# 6.2.5 删除键—值对 page 85

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']  # 注意 删除的键—值对永远消失了。
print(alien_0)

# 6.2.6 由类似对象组成的字典 page 86

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',  # 最后一个键—值对后面也加上逗号,为以后在下一行添加键—值对做好准备。
    }
print(favorite_languages)

'''请选择在合适的地方拆分要打印的内容,并在第一行末尾加上一个拼接运算符( +)。
按回车键进入print语句的后续各行,并使用Tab键将它们对齐并缩进一级。
指定要打印的所有内容后,在print语句的最后一行末尾加上右括号。
'''

print("sarah's favorite language is " +
    favorite_languages['sarah'].title() +
    ".")




