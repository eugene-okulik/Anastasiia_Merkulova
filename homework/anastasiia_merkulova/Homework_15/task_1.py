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
cursor.execute(
    "INSERT INTO students(name, second_name) VALUES (%s, %s)",
    (name, second_name)
)
student_id = cursor.lastrowid
print(f"student_id: {student_id}, name: {name}, second_name: {second_name}")

title = input('Enter group title: ')
start_date = input('Enter start date: ')
end_date = input('Enter end date: ')
cursor.execute(
    "INSERT INTO `groups`(title, start_date, end_date) VALUES (%s, %s, %s)",
    (title, start_date, end_date)
)
group_id = cursor.lastrowid
print(f"group_id: {group_id}, title: {title}, start_date: {start_date}, end_date: {end_date}")

books_count = int(input('Enter a number of books: '))
taken_by_student_id = student_id

books = []
for book in range(books_count):
    title = input(f"Enter book title: ")
    books.append((title, taken_by_student_id))
    print(f"title: {title}, taken_by_student_id: {taken_by_student_id}")

cursor.executemany(
"INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)",
books
)
book_id = cursor.lastrowid


cursor.execute(
    "UPDATE students SET group_id = %s WHERE id = %s",
    (group_id, student_id)
)


subjects_count = int(input('Enter a number of subjects: '))
for subject in range(subjects_count):
    subject_title = input('Enter subject title: ')
    cursor.execute(
        "INSERT INTO subjects (title) VALUES (%s)",
        (subject_title,)
    )
    subject_id = cursor.lastrowid

    for lesson in range(2):
        lesson_title = input(f"Enter lesson title {subject_title}: ")
        cursor.execute(
            "INSERT INTO lessons(title, subject_id) VALUES (%s, %s)",
            (lesson_title, subject_id)
        )
        lesson_id = cursor.lastrowid

        marks = []
        value = int(input(f"Enter mark for {lesson_title}:  "))
        cursor.executemany (
            "INSERT INTO marks(value, lesson_id, student_id) VALUES (%s, %s, %s)",
            [(value, lesson_id, student_id)]
        )
        marks_id = cursor.lastrowid

        print(f"marks_id: {marks_id}, value: {value}, lesson_id: {lesson_id}, "
              f"subject_id:{subject_id}, lesson_title: {lesson_title}, "
              f"student_id: {student_id}")


cursor.execute(
    """
    SELECT
        students.id AS student_id,
        students.name AS student_name,
        students.second_name AS student_second_name,
        `groups`.title AS group_title,
        `groups`.start_date AS group_start_date,
        `groups`.end_date AS group_end_date,
        books.title AS book_title,
        books.taken_by_student_id AS book_taken_by_student_id,
        subjects.title AS subject_title,
        lessons.title AS lesson_title,
        marks.value AS mark_value
    FROM students
    JOIN `groups` ON students.group_id = `groups`.id
    LEFT JOIN books ON students.id = books.taken_by_student_id
    LEFT JOIN marks ON students.id = marks.student_id
    LEFT JOIN lessons ON lessons.id = marks.lesson_id
    LEFT JOIN subjects ON lessons.subject_id = subjects.id
    WHERE students.id = %s
    """,
    (student_id,)
)

result = cursor.fetchall()

for row in result:
    print(row)


db.commit()
db.close()
