# 7.2 while 循环简介 page 104

# 7.2.1 使用 while 循环

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# 定义了一个退出值,只要用户输入的不是这个值,程序就接着运行
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

# 将变量message的初始值设置为空字符串 "",让Python首次执行while代码行时
# 有可供检查的东西。

message = ""

while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)

# 7.2.3 使用标志 page 106

'''
在要求很多条件都满足才继续运行的程序中,可定义一个变量,用于判断整个程序是否处于
活动状态。这个变量被称为标志,充当了程序的交通信号灯。你可让程序在标志为True时继续运
行,并在任何事件导致标志的值为False时让程序停止运行。这样,在while语句中就只需检查一
个条件——标志的当前值是否为True,并将所有测试(是否发生了应将标志设置为False的事件)
都放在其他地方,从而让程序变得更为整洁。
'''

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
active = True  # 用变量active来作为是否结束的标志

while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
