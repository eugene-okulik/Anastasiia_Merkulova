import os
from datetime import datetime, timedelta

base_path = os.path.dirname(__file__)
file_path = os.path.dirname(os.path.dirname(base_path))
eugene_path = os.path.join(file_path, 'eugene_okulik', 'hw_13', 'data.txt')
print(eugene_path)


def read_file():
    with open(eugene_path, 'r') as data_file:
        for line in data_file.readlines():
            yield line


for index, data_file in enumerate(read_file()):
    data_file = data_file.split()
    data_file = data_file[1] + ' ' + data_file[2]
    data_file = datetime.strptime(data_file, '%Y-%m-%d %H:%M:%S.%f')
    now = datetime.now()

    if index == 0:
        print(data_file + timedelta(days=7))
    elif index == 1:
        print(data_file.strftime('%A'))
    elif index == 2:
        print((now - data_file).days)
