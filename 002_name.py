# 2.3.1 使用方法修改字符串的大小写 page 19

# 方法 是Python可对数据执行的操作。

name = "ada lovelace"
print(name.title())  # title()以首字母大写的方式显示每个单词
print(name.lower())  # lower()将所有字母转换为小字
print(name.upper())  # upper()将所有字母转换为大写

# 2.3.2 合并(拼接)字符串 page 19

# 字符串的拼接
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)
print("Hello," + full_name.title() + "!")

message = "Hello," + full_name.title() + "!"
print(message)

# 2.3.3 使用制表符或换行符来添加空白 page 20

print("-" * 20)
# 空白泛指任何非打印字符,如空格、制表符和换行符。
# 在字符串中添加制表符,可使用字符组合\t

print("Python")
print("\tPython")

# 换行符： \n

print("language:\nPython\nC\njava\nc++")

print("language:\n\tPython\n\tC\n\tjava\n\tc++")

# 2.3.4 删除空白 page 21
print("-" * 20)

# 要确保字符串末尾没有空白,可使用方法rstrip()
favorite_language = 'python '
print(favorite_language + "abc")
print(favorite_language.rstrip() + "abc")


favorite_language = ' python '
print(favorite_language.rstrip())  # 删除右侧空格
print(favorite_language.lstrip())  # 删除左侧空格
print(favorite_language.strip())   # 删除前后空格




