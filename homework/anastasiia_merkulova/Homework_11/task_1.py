class Book:
    page_material = 'Standard paper'
    presence_of_text = True
    reserved = False

    def __init__(self, book_title, author, number_of_pages, isbn):
        self.book_title = book_title
        self.author = author
        self.number_of_pages = number_of_pages
        self.isbn = isbn

    def reserve_book(self):
        self.reserved = True

    def get_book_info(self):
        if self.reserved:
            print(f'Title: {self.book_title}\n'
                  f'Author: {self.author}\n'
                  f'Number of pages: {self.number_of_pages}\n'
                  f'Page material: {self.page_material}\n'
                  f'Is reserved?: {self.reserved}\n')
        else:
            print(f'Title: {self.book_title}\n'
                  f'Author: {self.author}\n'
                  f'Number of pages: {self.number_of_pages}\n'
                  f'Page material: {self.page_material}\n')


first_book = Book('The Silent Forest', 'Emma Carter', 320, '978-1-4028-9462-6')
second_book = Book('Journey to the Red Planet', 'Daniel Brooks', 280, '978-1-545-01022-1')
third_book = Book('The Art of Simple Living', 'Sophia Bennett', 210, '978-1-86197-876-9')
fourth_book = Book('Shadows of the Past', 'Michael Turner', 417, '978-0-7432-7356-5')
fifth_book = Book('Ocean Mysteries', 'laura Williams', 350, '978-1-250-30689-3')

first_book.reserve_book()


class SchoolBooks(Book):

    def __init__(self, book_title, author, number_of_pages, isbn, subject, grade, include_exercises):
        super().__init__(book_title, author, number_of_pages, isbn)
        self.subject = subject
        self.grade = grade
        self.include_exercises = include_exercises

    def get_book_info(self):
        if self.reserved:
            print(f'Title: {self.book_title}\n'
                  f'Author: {self.author}\n'
                  f'Number of pages: {self.number_of_pages}\n'
                  f'Subject: {self.subject}\n'
                  f'Grade: {self.grade}\n'
                  f'Is reserved?: {self.reserved}\n')
        else:
            print(f'Title: {self.book_title}\n'
                  f'Author: {self.author}\n'
                  f'Number of pages: {self.number_of_pages}\n'
                  f'Subject: {self.subject}\n'
                  f'Grade: {self.grade}\n')


first_schoolbook = SchoolBooks('Mathematics,Grade 10', 'Emma Smith', 280, '918-1-4028-9462-6', 'Mathematics', 10, True)
second_schoolbook = SchoolBooks('History Grade 9', 'Jim Taylor', 310, '918-1-4028-9002-6', 'History', 12, False)

first_schoolbook.reserve_book()

first_book.get_book_info()
second_book.get_book_info()
third_book.get_book_info()
fourth_book.get_book_info()
fifth_book.get_book_info()

first_schoolbook.get_book_info()
second_schoolbook.get_book_info()
