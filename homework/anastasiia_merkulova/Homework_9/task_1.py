import datetime
my_time = 'Jan 15, 2023 - 12:05:33'
python_date = datetime.datetime.strptime(my_time, '%b %d, %Y - %H:%M:%S')
human_month = python_date.strftime('%B')
date_format = python_date.strftime('%d.%m.%Y, %H:%M')

print(python_date)
print(human_month)
print(date_format)
