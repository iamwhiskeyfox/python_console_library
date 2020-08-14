from DB.adapter import BookDBAdapter
import sqlite3
from models import Book


class SqliteBooksDbAdapter(BookDBAdapter):
    def __init__(self, filename):
        self.filename = filename
        self.connection = None

        super().__init__()

    def prepare(self):
        self.connection = sqlite3.connect(self.filename)
        self._create_tables()

    def _create_tables(self):
        cursor = self.connection.cursor()
        cursor.execute("""
        
        CREATE TABLE IF NOT EXISTS Books(id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT,
                       year INTEGER,
                       author TEXT,
                       genre TEXT)  
                       
                       """)
        self.connection.commit()

    def get_all_books(self) -> list:
        cursor = self.connection.cursor()
        rows = cursor.execute("SELECT * FROM Books")
        books = []
        for row in rows:
            book = Book(row[1], int(row[2]), row[3], row[4])
            book.id = int(row[0])
            books.append(book)

        return books

    def save_new_book(self, book: Book):
        cursor = self.connection.cursor()
        cursor.execute('INSERT INTO Books(name,year,author,genre) VALUES(?,?,?,?)',
                       (book.name, book.year, book.author, book.genre))
        self.connection.commit()
