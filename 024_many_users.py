# 6.4.3 在字典中存储字典 page 97

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    # 转义字符\t是让python生成一个tab键
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
