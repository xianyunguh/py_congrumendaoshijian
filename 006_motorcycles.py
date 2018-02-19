# 3.2 修改、添加和删除元素 page 33

# 3.2.1 修改列表元素 page 34

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# 3.2.2 在列表中添加元素 page 34

# 1. 在列表末尾添加元素

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

# 给空列表添加元素

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# 2. 在列表中插入元素

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

# 3.2.3 从列表中删除元素

# 1. 使用del语句删除元素

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[1]
print(motorcycles)

# 2. 使用方法pop()删除元素

'''
方法pop()可删除列表末尾的元素,并让你能够接着使用它。
术语弹出(pop)源自这样的类比:
列表就像一个栈,而删除列表末尾的元素相当于弹出栈顶元素。
'''

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " +
      last_owned.title() + ".")

# 3. 弹出列表中任何位置处的元素

motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' +
    first_owned.title() + '.')

'''
如果你不确定该使用del语句还是pop()方法,下面是一个简单的判断标准:
如果你要从列表中删除一个元素,且不再以任何方式使用它,就使用del 语句;
如果你要在删除元素后还能继续使用它,就使用方法pop()。
'''

# 4. 根据值删除元素

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

'''
注意方法remove() 只删除第一个指定的值。如果要删除的值可能在列表中
出现多次,就需要使用循环来判断是否删除了所有这样的值。
'''
