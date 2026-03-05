class Book:
    page_material = 'Standard paper'
    presence_of_text = True

    def __init__(self, book_title, author, number_of_pages, isbn, reserved):
        self.book_title = book_title
        self.author = author
        self.number_of_pages = number_of_pages
        self.isbn = isbn
        self.reserved = reserved

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

first_book = Book('The Silent Forest', 'Emma Carter', 320, '978-1-4028-9462-6', True)
second_book = Book('Journey to the Red Planet', 'Daniel Brooks', 280, '978-1-545-01022-1', False)
third_book = Book('The Art of Simple Living', 'Sophia Bennett', 210, '978-1-86197-876-9', False)
fourth_book = Book('Shadows of the Past', 'Michael Turner', 417, '978-0-7432-7356-5', False)
fifth_book = Book('Ocean Mysteries', 'laura Williams', 350, '978-1-250-30689-3', False)

first_book.get_book_info()
second_book.get_book_info()
third_book.get_book_info()
fourth_book.get_book_info()
fifth_book.get_book_info()

