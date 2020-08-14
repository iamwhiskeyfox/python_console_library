from books_app import BooksApp
from DB.adapter import BookDBAdapter
from DB.sqlite_adapter import SqliteBooksDbAdapter
if __name__ == '__main__':
    adapter = SqliteBooksDbAdapter('books.db')
    app = BooksApp(adapter)
    app.start()

