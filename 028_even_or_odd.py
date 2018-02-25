# 7.1.3 求模运算符　page 103

# 求模运算符(%)将两个数相除并返回余数

# 判断输入的数是偶数还是奇数。
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")

# 7.1.4 在 Python 2.7 中获取输入 page 104

'''
如果你使用的是Python 2.7,应使用函数raw_input()来提示用户输入。
这个函数与Python 3中的input()一样,也将输入解读为字符串。

Python 2.7也包含函数input(),但它将用户输入解读为Python代码,
并尝试运行它们。
'''
