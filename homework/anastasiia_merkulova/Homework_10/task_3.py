first = int(input("Введите первое число: "))
second = int(input("Введите второе число:"))


def select_decorator(func):
    def wrapper(first, second, operation):
        if first < 0 or second < 0:
            operation = '*'
        elif first > second:
            operation = '-'
        elif second > first:
            operation = '/'
        elif first == second:
            operation = '+'
        return func(first, second, operation)
    return wrapper


@select_decorator
def calc(first, second, operation):
    if operation == '*':
        return first * second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    else:
        return first + second


print(calc(first, second, '+'))
