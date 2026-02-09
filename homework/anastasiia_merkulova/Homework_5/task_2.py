all_text_one = 'результат операции: 42'
number_index_one = all_text_one.index(':')
number_one = int(all_text_one[number_index_one + 1:]) + 10

print(number_one)

all_text_two = 'результат операции: 514'
number_index_two = all_text_two.index(':')
number_two = int(all_text_two[number_index_two + 1:]) + 10

print(number_two)

all_text_three = 'результат работы операции: 9'
number_index_three = all_text_three.index(':')
number_three = int(all_text_three[number_index_three + 1:]) + 10

print(number_three)
