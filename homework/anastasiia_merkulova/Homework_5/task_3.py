students = ['Ivanov', 'Petrov', 'Sidorov']
students = ', '.join(students)
subjects = ['math', 'biology', 'geography']
subjects = ', '.join(subjects)
my_text = 'Students {0} study these subjects: {1}'

print(my_text.format(students, subjects))
