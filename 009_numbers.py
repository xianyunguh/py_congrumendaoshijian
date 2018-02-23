# 4.3 创建数值列表 page 51

# 4.3.1 使用函数 range() page 51

# 函数range()让Python从你指定的第一个值开始数,
# 并在到达你指定的第二个值后停止,因此输出不包含第二个值(这里为5) 。

for value in range(1,5):
    print(value)

# 4.3.2 使用 range() 创建数字列表 page 51

# 函数list()将range()的结果直接转换为列表

numbers = list(range(1,6))
print(numbers)

