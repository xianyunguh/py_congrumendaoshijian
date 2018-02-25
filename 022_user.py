# 6.3 遍历字典 page 87

# 遍历字典的方式:可遍历字典的所有键—值对、键或值。

# 6.3.1 遍历所有的键—值对

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():  # 方法items()返回一个键—值对列表。
    print("\nKey: " + key)
    print("Value: " + value)

'''
注意,即便遍历字典时,键—值对的返回顺序也与存储顺序不同。Python不关心键—值对的存
储顺序,而只跟踪键和值之间的关联关系。
'''

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
        language.title() + ".")


# 6.3.2 遍历字典中的所有键 page 89

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

# keys()返回字典中的键，遍历字典时,会默认遍历所有的键,因此,这里的key()是可以省略的。
for name in favorite_languages.keys():
    print(name.title())

# ----------------

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

friends = ['phil', 'sarah']

for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print(" Hi " + name.title() +
            ", I see your favorite language is " +
            favorite_languages[name].title() + "!")

# ---------------

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

# 方法keys()并非只能用于遍历;实际上,它返回一个列表,其中包含字典中的所有键,
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

# 6.3.3 按顺序遍历字典中的所有键 page 91

