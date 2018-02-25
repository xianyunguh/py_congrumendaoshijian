# 7.1.2 使用 int()来获取数值输入 page 102

# 函数 int()将数字的字符串表示转换为数值

height = input("How tall are you, in inches? ")
height = int(height)

if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")



