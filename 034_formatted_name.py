# 8.3 返回值  page 121

# 在函数中,可使用return语句将值返回到调用函数的代码行。

# 8.3.1 返回简单值


def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# 8.3.2 让实参变成可选的 page 122

# 可使用默认值来让实参变成可选的。


def get_formatted_name(first_name, middle_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

'''
为让get_formatted_name()在没有提供中间名时依然可行,
可给实参middle_name指定一个默认值——空字符串,并将其移到形参列表的末尾:

'''


def get_formatted_name(first_name, last_name, middle_name=''):
    """返回整洁的姓名"""
    if middle_name:  # Python将非空字符串解读为True
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
