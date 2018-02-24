# 5.2.7 检查特定值是否不包含在列表中 page 69

# 确定特定的值未包含在列表中可使用关键字not in。

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")

# 5.2.8 布尔表达式 page 69

game_active = True
can_edit = False
