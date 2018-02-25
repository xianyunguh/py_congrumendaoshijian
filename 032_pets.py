# 7.3.2 删除包含特定值的所有列表元素 page 111

'''
在第3章中,我们使用函数remove()来删除列表中的特定值,这之所以可行,
是因为要删除的值在列表中只出现了一次。
如果要删除列表中包含多个重复元素,该怎么办呢?
'''

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:  # 只要列表中有 cat　值，条件即为真。
    pets.remove('cat')
    print(pets)
