# 5.2.4 比较数字 page 67

answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")

# 5.2.5 检查多个条件 page 67

# 使用and检查多个条件

age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)

age_1 = 22
print(age_0 >= 21 and age_1 >= 21)  # 为改善可读性,可将每个测试都分别放在一对括号内

# 2. 使用or检查多个条件

# 5.2.6 检查特定值是否包含在列表中 page 68

# 要判断特定的值是否已包含在列表中,可使用关键字in。

requested_toppings = ['mushrooms', 'onions', 'pineapple']

print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)






