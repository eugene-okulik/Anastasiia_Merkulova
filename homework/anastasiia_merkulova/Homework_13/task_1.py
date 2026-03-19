import os
import datetime

base_path = os.path.dirname(__file__)
file_path = os.path.dirname(os.path.dirname(base_path))
eugene_path = os.path.join(file_path, 'eugene_okulik','hw_13', 'data.txt')
print(eugene_path)

def read_file():
    with open(eugene_path, 'r') as data_file:
        for line in data_file.readlines():
            yield line

for data_file in read_file():
    data_file = data_file.split()
    data_file = data_file[1] +  ' ' + data_file[2]
    print(data_file)

strip склеить строки и поменять даты









