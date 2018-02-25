# 6.4.2 在字典中存储列表 page 96

# 存储所点比萨的信息
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }

# 概述所点的比萨
print("You ordered a " + pizza['crust'] + "-crust pizza " +
      "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)

# 每当需要在字典中将一个键关联到多个值时,都可以在字典中嵌套一个列表。

'''
在本章前面有关喜欢的编程语言的示例中,如果将每个人的回答都存储在一个列表中,
被调查者就可选择多种喜欢的语言。
'''

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }

for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())


