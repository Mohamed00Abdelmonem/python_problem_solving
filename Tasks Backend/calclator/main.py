def add(a, b):
    """the add two numbers """
    return a + b


def sub(a, b):
    """the sub two numbers """
    return a - b


def multiply(a, b):
    """the multiply two numbers """
    return a * b


def divide(a, b):
    """the divide two numbers """
    return a / b


operation = {"+": add,
             "-": sub,
             "*": multiply,
             "/": divide}

user_input_first = int(input("Enter your first number: "))

user_input_second = int(input("Enter your second number: "))
user_operation = input("Enter your operation : ")

calc_function = operation[user_operation]
answer = calc_function(user_input_first, user_input_second)
print(f"answer = {answer}")
