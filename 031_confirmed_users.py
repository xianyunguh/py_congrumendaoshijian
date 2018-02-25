# 7.2.6 避免无限循环 page 109

'''
注意有些编辑器(如Sublime Text)内嵌了输出窗口,这可能导致难以结束无限循环,因此不
得不关闭编辑器来结束无限循环。
'''

# 7.3 使用 while 循环来处理列表和字典 page 110

'''
for循环是一种遍历列表的有效方式,但在for循环中不应修改列表,否则将导致Python难以
跟踪其中的元素。要在遍历列表的同时对其进行修改,可使用while循环。通过将while循环同列
表和字典结合起来使用,可收集、存储并组织大量输入,供以后查看和显示。
'''

# 7.3.1 在列表之间移动元素

# 首先,创建一个待验证用户列表
# 和一个用于存储已验证用户的空列表
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# 验证每个用户,直到没有未验证用户为止
# 将每个经过验证的列表都移到已验证用户列表中
while unconfirmed_users:
    # 函 数 pop() 以 每 次 一 个 的 方 式 从 列 表末尾删除
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

# 显示所有已验证的用户
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
