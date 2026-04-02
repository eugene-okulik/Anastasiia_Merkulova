import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

name = input('Enter your name: ')
second_name = input('Enter your second name: ')


cursor = db.cursor(dictionary=True)
cursor.execute("INSERT INTO students(name, second_name) VALUES (%s, %s)",
(name, second_name)
)
student_id = cursor.lastrowid
print(f"student_id: {student_id}, name: {name}, second_name: {second_name}")

title = input('Enter group title: ')
start_date = input('Enter start date: ')
end_date = input('Enter end date: ')
cursor.execute("INSERT INTO `groups`(title, start_date, end_date) VALUES (%s, %s, %s)",
(title, start_date, end_date)
)
group_id = cursor.lastrowid
print(f"group_id: {group_id}, title: {title}, start_date: {start_date}, end_date: {end_date}")

books_count = int(input('Enter a number of books: '))
taken_by_student_id = student_id
for book in range(books_count):
    book_title = input('Enter book title: ')
    cursor.execute("INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)",
(book_title, taken_by_student_id )
)
    book_id = cursor.lastrowid
    print(f"book_id: {book_id}, title: {book_title}, taken_by_student_id: {taken_by_student_id}")

cursor.execute("UPDATE students SET group_id = %s WHERE id = %s",
(group_id, student_id)
)


subjects_count = int(input('Enter a number of subjects: '))
for subject in range(subjects_count):
    subject_title = input('Enter subject title: ')
    cursor.execute("INSERT INTO subjects (title) VALUES (%s)",
    (subject_title,)
    )
    subject_id = cursor.lastrowid

    for lesson in range(2):
        lesson_title = input(f"Enter lesson title {subject_title}: ")
        cursor.execute("INSERT INTO lessons(title, subject_id) VALUES (%s, %s)",
        (lesson_title,subject_id)
        )
        lesson_id = cursor.lastrowid

        value = int(input(f"Enter mark for {lesson_title}:  "))
        cursor.execute("INSERT INTO marks(value, lesson_id, student_id) VALUES (%s, %s, %s)",
        (value, lesson_id, student_id)
        )
        marks_id = cursor.lastrowid
        print(f"marks_id: {marks_id}, value: {value}, lesson_id: {lesson_id}, "
              f"subject_id:{subject_id}, lesson_title: {lesson_title}, "
              f"student_id: {student_id}")

db.commit()
db.close()
