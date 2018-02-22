# 3.3 组织列表 page 39

# 3.3.1 使用方法 sort()对列表进行永久性排序 page 39

cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)

cars.sort(reverse = True) #倒序排列
print(cars)

# 3.3.2 使用函数 sorted()对列表进行临时排序 page 40

# sorted()让你能够按特定顺序显示列表元素,同时不影响它们在列表中的原始排列顺序。

cars = ['bmw','audi','toyota','subaru']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list:")
print(cars)

# 3.3.3 倒着打印列表 page 41

cars = ['bmw','audi','toyota','subaru']
print(cars)

cars.reverse()
print(cars)

# 3.3.4 确定列表的长度 page 41

print(len(cars))

# 3.4  使用列表时避免索引错误 page 42

# 索引-1总是返回最后一个列表元素

print(cars[-1])

motorcycles = []
print(motorcycles[-1]) # 列表为空时，索引-1会引发错误


