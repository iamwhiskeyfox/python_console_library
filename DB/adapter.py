from models import Book


class BookDBAdapter:
    def __init__(self):
        self.books = []

    def prepare(self):
        pass

    def get_all_books(self) -> list:
        return self.books

    def save_new_book(self, book: Book):
        self.books.append(book)

    def get_book_by_id(self, id) -> Book or None:
        for book in self.books:
            if book.id == id:
                return book
        return None

    def delete_book(self, id):
        for book in self.books:
            if book.id == id:
                self.books.remove(book)
                break

    def update_book(self, updated_book: Book):
        for book in self.books:
            if book == updated_book.id:
                book.name = updated_book.name
                book.year = updated_book.year
                book.author = updated_book.author
                book.genre = updated_book.genre
                break
