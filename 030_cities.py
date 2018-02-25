# 7.2.4 使用 break 退出循环 page 107

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")

'''
注意在任何Python循环中都可使用break语句。
例如,可使用break语句来退出遍历列表或字典的for循环。
'''

# 7.2.5 在循环中使用 continue  page 108

current_number = 0

while current_number < 10:
    current_number += 1

    if current_number % 2 == 0:
        continue

    print(current_number)

