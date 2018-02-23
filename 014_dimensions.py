# 4.5 元组 page 59

# 不可变的列表被称为元组。

# 4.5.1 定义元组

dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

# 4.5.2 遍历元组中的所有值

dimensions = (200,50)
for dimension in dimensions:
    print(dimension)

# 4.5.3 修改元组变量

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

'''
相比于列表,元组是更简单的数据结构。如果需要存储的一组值在程序的整个生命周期内都
不变,可使用元组。

'''

# 4.6  设置代码格式 page 61
# 4.6.1 格式设置指南
# 4.6.2 缩进
'''
PEP 8建议每级缩进都使用四个空格,

但混合使用制表符和空格会让Python解释器感到迷惑。
每款文本编辑器都提供了一种设置,可将输入的制表符转换为指定数量的空格。
你在编写代码时应该使用制表符键,但一定要
对编辑器进行设置,使其在文档中插入空格而不是制表符。

'''

# 4.6.3 行长

'''
很多Python程序员都建议每行不超过80字符。
专业程序员通常会在同一个屏幕上打开多个文件,使用标准行长可以让他们在屏幕上并排
打开两三个文件时能同时看到各个文件的完整行。
PEP 8还建议注释的行长都不超过72字符,因为有些工具为大型项目自动生成文档时,
会在每行注释开头添加格式化字符。


'''

# 4.6.4 空行
