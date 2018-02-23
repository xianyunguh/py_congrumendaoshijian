# 4.4.3 复制列表 page 56

# 创建一个包含整个列表的切片,方法是同时省略起始索引和终止索引([:])。

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

'''
 friend_foods = my_foods
这种语法实际上是让Python将新变量friend_foods关联到包含在my_foods中的列表,
因此这两个变量都指向同一个列表。鉴于此,当我们将 'cannoli' 添加到 my_foods 
中时,它也将出现在friend_foods中;同样,虽然 'ice cream'好像只被加入到了
friend_foods中,但它也将出现在这两个列表中。
'''

