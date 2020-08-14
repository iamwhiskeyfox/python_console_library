from books_app import BooksApp
from DB.adapter import BookDBAdapter
if __name__ == '__main__':
    adapter = BookDBAdapter()
    app = BooksApp(adapter)
    app.start()

