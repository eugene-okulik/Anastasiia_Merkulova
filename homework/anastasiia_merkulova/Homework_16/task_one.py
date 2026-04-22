import mysql.connector as mysql
import os
import csv
import dotenv

dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_DATABASE')
)

cursor = db.cursor(dictionary=True)

base_path = os.path.dirname(__file__)
file_path = os.path.dirname(os.path.dirname(base_path))
anastasiia_path = os.path.join(file_path, 'eugene_okulik', 'lesson_16', 'hw_data', 'data.csv')
with open(anastasiia_path, newline='') as csv_file:
    file_data = csv.DictReader(csv_file)
    for row in file_data:
        cursor.execute(
            '''
        SELECT
        students.name AS student_name,
        students.second_name AS second_name,
        `groups`.title AS group_title,
        books.title AS book_title,
        subjects.title AS subject_title,
        lessons.title AS lesson_title,
        marks.value as mark_value
        FROM students
        LEFT JOIN books ON students.id = books.taken_by_student_id
        LEFT JOIN `groups` ON students.group_id = `groups`.id
        LEFT JOIN marks ON students.id = marks.student_id
        LEFT JOIN lessons ON marks.lesson_id = lessons.id
        LEFT JOIN subjects ON lessons.subject_id = subjects.id
        WHERE students.name = %s
        AND students.second_name = %s
        AND `groups`.title = %s
        AND books.title = %s
        AND subjects.title = %s
        AND lessons.title = %s
        AND marks.value = %s
            ''',
            (
                row['name'],
                row['second_name'],
                row['group_title'],
                row['book_title'],
                row['subject_title'],
                row['lesson_title'],
                row['mark_value'],
            )
        )
        result = cursor.fetchall()
        if result:
            print(result)
        else:
            print("No data")
