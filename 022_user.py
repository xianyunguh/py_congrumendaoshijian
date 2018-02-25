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
        print(" Hi " + name.title()+
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

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

# sorted()让Python在遍历前对这个列表进行排序。
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

# 6.3.4 遍历字典中的所有值 page 91

# 方法values(),返回一个值列表,而不包含任何键。

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

print("The following languages have been mentioned:")

for language in favorite_languages.values():
    print(language.title())

# 为剔除重复项,可使用集合(set)。
'''
通过对包含重复元素的列表调用set() ,可让Python找出列表中独一无二的元素,
并使用这些元素来创建一个集合。
'''

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

print("The following languages have been mentioned:")

for language in set(favorite_languages.values()):
    print(language.title())

# 6.4 嵌套 page 93

# 6.4.1 字典列表

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# 使用range()生成了30个外星人

# 创建一个用于存储外星人的空列表

aliens = []

# 创建30个绿色的外星人
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# 显示前五个外星人
for alien in aliens[:5]:
    print(alien)
print("...")

# 显示创建了多少个外星人
print("Total number of aliens: " + str(len(aliens)))


# 要将前三个外星人修改为黄色的、速度为中等且值10个点,

# 创建一个用于存储外星人的空列表
aliens = []

# 创建30个绿色的外星人
for alien_number in range (0,30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# 显示前五个外星人
for alien in aliens[0:5]:
    print(alien)

print("...")

# 中添加一个elif代码块,将黄色外星人改为移动速度快且值15个点的红色外星人,
'''
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
'''


