# 将1-10的平方加入到一个列表中

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)

print(squares)

# 下面是简化后的程序

squares = []
for value in range(1,11):
    squares.append(value**2)

print(squares)

# 4.3.3 对数字列表执行简单的统计计算 page 53

digits = [1,2,3,4,5,6,7,8,9,10]

print(min(digits))
print(max(digits))
print(sum(digits))

# 4.3.4 列表解析  page 53

'''
前面介绍的生成列表 squares 的方式包含三四行代码,而列表解析让你只需编写
一行代码就能生成这样的列表。列表解析将for循环和创建新元素的代码合并成一行,
并自动附加新元素。
'''

squares = [value**2 for value in range(1,11)]
print(squares)



