def right_number(program_number):
    while True:
        my_number = int(input('Enter a number:'))
        if my_number == program_number:
         print('Поздравляю!Вы угадали!')
         break
        elif my_number != program_number:
         print('Попробуйте снова!')
right_number(100)










