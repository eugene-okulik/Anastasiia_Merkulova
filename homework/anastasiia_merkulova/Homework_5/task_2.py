all_text_one = 'результат операции: 42'
list_from_all_text_one = all_text_one.split()
result_one = list_from_all_text_one[-1]
result_one = int(result_one) + 10

print(result_one)

all_text_two = 'результат операции: 514'
list_from_all_text_two = all_text_two.split()
result_two = list_from_all_text_two[-1]
result_two = int(result_two) + 10

print(result_two)

all_text_three = 'результат работы операции: 9'
list_from_all_text_three = all_text_three.split()
result_three = list_from_all_text_three[-1]
result_three = int(result_three) + 10

print(result_three)
