# 4.4 使用列表的一部分 page 54

# 4.4.1 切片  page 54

"""
要创建切片, 可指定要使用的第一个元素和最后一个元素的索引。
与函数range()一样, Python在到达你指定的第二个索引前面的元素后停止。
要输出列表中的前三个元素,需要指定索引0~3
"""

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[2:4])
print(players[:3])  # 如果你没有指定第一个索引,Python将自动从列表开头开始
print(players[1:])  # 不指定结尾则到列表的最后一个
print(players[-3:])  # 负数索引返回离列表末尾相应距离的元素

# 4.4.2 遍历切片 page 56

players = ['charles','martina','michael','florence','eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

