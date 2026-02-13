def count_numbers(string):
    string = string.split(' ')
    return int(string[-1]) + 10

print(count_numbers('результат операции: 42'))
print(count_numbers('результат операции: 54'))
print(count_numbers('результат работы программы: 209'))
print(count_numbers('результат: 2'))
