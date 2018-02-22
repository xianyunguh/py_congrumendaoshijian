# 3.1 列表是什么 page 31

# 鉴于列表通常包含多个元素,给列表指定一个表示复数的名称
#  (如letters、 digits或names)是个不错的主意。

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# 3.1.1 访问列表元素 page 32

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())

# 3.1.2 索引从 0 而不是 1 开始  page 32

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[1])
print(bicycles[3])

# 通过将索引指定为-1,可让Python返回最后一个列表元素:
'''
这种语法很有用,因为你经常需要在不知道列表长度的情况
下访问最后的元素。这种约定也适用于其他负数索引,
例如,索引-2返回倒数第二个列表元素,
索引-3返回倒数第三个列表元素,以此类推。
'''

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1])

# 3.1.3 使用列表中的各个值 page 33

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)



