# 7.1.1 编写清晰的程序 page 101

name = input("Please enter your name: ")
print("Hello, " + name + "!")

# 提示超过一行

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)

print("\nHello, " + name + "!")


